﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Lro"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError
from msrest.authentication import BasicTokenAuthentication
from msrest.polling import LROPoller
from msrestazure.azure_exceptions import CloudError, CloudErrorData
from msrestazure.polling.arm_polling import ARMPolling

from lro import AutoRestLongRunningOperationTestService
from lro.models import *  # pylint: disable=W0614


try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import pytest

class AutorestTestARMPolling(ARMPolling):

    def _polling_cookie(self, response):
        """Collect retry cookie - we only want to do this for the test server
        at this point, unless we implement a proper cookie policy.

        :returns: Dictionary containing a cookie header if required,
         otherwise an empty dictionary.
        """
        parsed_url = urlparse(response.request.url)
        host = parsed_url.hostname.strip('.')
        if host == 'localhost':
            return {'cookie': response.headers.get('set-cookie', '')}
        return {}

    def request_status(self, status_link):
        request = self._client.get(status_link)
        # ARM requires to re-inject 'x-ms-client-request-id' while polling
        header_parameters = {
            'x-ms-client-request-id': self._operation.initial_response.request.headers['x-ms-client-request-id']
        }
        header_parameters.update(self._polling_cookie(self._response))
        return self._client.send(request, header_parameters, stream=False)

@pytest.fixture()
def client():
    """Create a AutoRestLongRunningOperationTestService client with test server credentials."""
    cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
    with AutoRestLongRunningOperationTestService(cred, base_url="http://localhost:3000") as client:
        client.config.long_running_operation_timeout = 0 # In theory pointless, since we use AutorestTestARMPolling
        yield client

@pytest.fixture()
def special_client(client, test_session_callback):
    client.config.session_configuration_callback = test_session_callback
    return client


class TestLro:

    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            self.lro_result(func, *args, **kwargs)
            pytest.fail("CloudError wasn't raised as expected")

        except CloudError as err:
            assert msg in  err.message
            assert err.response is not None
            error = err.error
            assert error is not None
            if isinstance(error, CloudErrorData):
                assert error.message is not None

    def lro_result(self, func, *args, **kwargs):
        if "polling" not in kwargs:
            kwargs["polling"] = AutorestTestARMPolling(0)
        return func(*args, **kwargs).result()

    def test_lro_post_issue(self, client):
        product = client.lr_os.post_double_headers_final_location_get().result()
        assert product.id == "100"

        product = client.lr_os.post_double_headers_final_azure_header_get().result()
        assert product.id == "100"

    def test_lro_happy_paths(self, special_client):
        client = special_client

        product = Product(location="West US")

        process = self.lro_result(client.lr_os.put201_creating_succeeded200, product)
        assert "Succeeded" ==  process.provisioning_state

        # Test manual poller
        raw_process = client.lr_os.put201_creating_succeeded200(product, raw=True, polling=False).result()
        poller = LROPoller(client, raw_process, Product, ARMPolling(timeout=0))
        process = poller.result()
        assert "Succeeded" ==  process.provisioning_state

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            client.lr_os.put201_creating_failed200, product)

        process = self.lro_result(client.lr_os.put200_updating_succeeded204, product)
        assert "Succeeded" ==  process.provisioning_state

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            client.lr_os.put200_acceptedcanceled200, product)

        # Testing nopolling
        process = self.lro_result(client.lr_os.put201_creating_succeeded200, product, polling=False)
        assert "Creating" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put201_creating_failed200, product, polling=False)
        assert "Created" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put200_updating_succeeded204, product, polling=False)
        assert "Updating" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put200_acceptedcanceled200, product, polling=False)
        assert "Accepted" ==  process.provisioning_state

        # Testing nopolling and raw at the same time
        process = self.lro_result(client.lr_os.put201_creating_succeeded200, product, raw=True, polling=False)
        assert "Creating" ==  process.output.provisioning_state

        process = self.lro_result(client.lr_os.put201_creating_failed200, product, raw=True, polling=False)
        assert "Created" ==  process.output.provisioning_state

        process = self.lro_result(client.lr_os.put200_updating_succeeded204, product, raw=True, polling=False)
        assert "Updating" ==  process.output.provisioning_state

        process = self.lro_result(client.lr_os.put200_acceptedcanceled200, product, raw=True, polling=False)
        assert "Accepted" ==  process.output.provisioning_state

        process = self.lro_result(client.lr_os.put_no_header_in_retry, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put_async_no_header_in_retry, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put_sub_resource, SubProduct())
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put_async_sub_resource, SubProduct())
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put_non_resource, Sku())
        assert "100" ==  process.id

        process = self.lro_result(client.lr_os.put_async_non_resource, Sku())
        assert "100" ==  process.id

        process = self.lro_result(client.lr_os.post202_retry200, product)
        assert process is None

        process = self.lro_result(client.lr_os.put200_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put200_succeeded_no_state, product)
        assert "100" ==  process.id

        process = self.lro_result(client.lr_os.put202_retry200, product)
        assert "100" ==  process.id

        process = self.lro_result(client.lr_os.put_async_retry_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

        process = self.lro_result(client.lr_os.put_async_no_retry_succeeded, product)
        assert "Succeeded" ==  process.provisioning_state

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            client.lr_os.put_async_retry_failed, product)

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            client.lr_os.put_async_no_retrycanceled, product)

        assert self.lro_result(client.lr_os.delete204_succeeded) is None
        assert self.lro_result(client.lr_os.delete202_retry200) is None
        assert self.lro_result(client.lr_os.delete202_no_retry204) is None

        assert self.lro_result(client.lr_os.delete_async_no_retry_succeeded) is None
        assert self.lro_result(client.lr_os.delete_no_header_in_retry) is None

        assert self.lro_result(client.lr_os.delete_async_no_header_in_retry) is None

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            client.lr_os.delete_async_retrycanceled)

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Failed",
            client.lr_os.delete_async_retry_failed)

        assert self.lro_result(client.lr_os.delete_async_retry_succeeded) is None

        process = self.lro_result(client.lr_os.delete_provisioning202_accepted200_succeeded)
        assert "Succeeded" ==  process.provisioning_state

        result = self.lro_result(client.lr_os.delete_provisioning202_deletingcanceled200)
        assert result.provisioning_state ==  'Canceled'

        result = self.lro_result(client.lr_os.delete_provisioning202_deleting_failed200)
        assert result.provisioning_state ==  'Failed'

        assert self.lro_result(client.lr_os.post202_no_retry204, product) is None

        self.assertRaisesWithMessage("Internal Server Error",
            client.lr_os.post_async_retry_failed)

        self.assertRaisesWithMessage("Operation failed with status: 200. Details: Resource state Canceled",
            client.lr_os.post_async_retrycanceled)

        prod = self.lro_result(client.lr_os.post_async_retry_succeeded)
        assert prod.id ==  "100"

        prod = self.lro_result(client.lr_os.post_async_no_retry_succeeded)
        assert prod.id ==  "100"

        sku = self.lro_result(client.lr_os.post200_with_payload)
        assert sku.id ==  '1'

        process = self.lro_result(client.lro_retrys.put201_creating_succeeded200, product)
        assert 'Succeeded' ==  process.provisioning_state

        process = self.lro_result(client.lro_retrys.put_async_relative_retry_succeeded, product)
        assert 'Succeeded' ==  process.provisioning_state

        process = self.lro_result(client.lro_retrys.delete_provisioning202_accepted200_succeeded)
        assert 'Succeeded' ==  process.provisioning_state

        assert self.lro_result(client.lro_retrys.delete202_retry200) is None
        assert self.lro_result(client.lro_retrys.delete_async_relative_retry_succeeded) is None
        assert self.lro_result(client.lro_retrys.post202_retry200, product) is None
        assert self.lro_result(client.lro_retrys.post_async_relative_retry_succeeded, product) is None

        custom_headers = {"x-ms-client-request-id": '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}

        process = self.lro_result(client.lr_os_custom_header.put_async_retry_succeeded, product, custom_headers)
        assert process is not None

        process = self.lro_result(client.lr_os_custom_header.post_async_retry_succeeded, product, custom_headers)
        assert process is None

        process = self.lro_result(client.lr_os_custom_header.put201_creating_succeeded200, product, custom_headers)
        assert process is not None

        process = self.lro_result(client.lr_os_custom_header.post202_retry200, product, custom_headers)
        assert process is None

    def test_lro_sad_paths(self, client):

        product = Product(location="West US")

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.put_non_retry400, product)

        self.assertRaisesWithMessage("Error from the server",
            client.lrosa_ds.put_non_retry201_creating400, product)

        self.assertRaisesWithMessage("Operation failed with status: 'Bad Request'",
            client.lrosa_ds.put_async_relative_retry400, product)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.delete_non_retry400)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.delete202_non_retry400)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.delete_async_relative_retry400)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.post_non_retry400, product)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.post202_non_retry400, product)

        self.assertRaisesWithMessage("Expected bad request message",
            client.lrosa_ds.post_async_relative_retry400, product)

        self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            client.lrosa_ds.put_error201_no_provisioning_state_payload, product)

        self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            client.lrosa_ds.put_async_relative_retry_no_status, product)

        self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            client.lrosa_ds.put_async_relative_retry_no_status_payload, product)

        with pytest.raises(DeserializationError):
            self.lro_result(client.lrosa_ds.put200_invalid_json, product)

        with pytest.raises(DeserializationError):
            self.lro_result(client.lrosa_ds.put_async_relative_retry_invalid_json_polling, product)

        with pytest.raises(Exception):
            self.lro_result(client.lrosa_ds.put_async_relative_retry_invalid_header, product)

        with pytest.raises(Exception):
            self.lro_result(client.lrosa_ds.delete202_retry_invalid_header)

        with pytest.raises(Exception):
            self.lro_result(client.lrosa_ds.delete_async_relative_retry_invalid_header)

        with pytest.raises(Exception):
            self.lro_result(client.lrosa_ds.post202_retry_invalid_header)

        with pytest.raises(Exception):
            self.lro_result(client.lrosa_ds.post_async_relative_retry_invalid_header)

        with pytest.raises(DeserializationError):
            self.lro_result(client.lrosa_ds.delete_async_relative_retry_invalid_json_polling)

        with pytest.raises(DeserializationError):
            self.lro_result(client.lrosa_ds.post_async_relative_retry_invalid_json_polling)

        self.lro_result(client.lrosa_ds.delete204_succeeded)

        self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            client.lrosa_ds.delete_async_relative_retry_no_status)

        self.assertRaisesWithMessage("Unable to find status link for polling.",
            client.lrosa_ds.post202_no_location)

        self.assertRaisesWithMessage("The response from long running operation does not contain a body.",
            client.lrosa_ds.post_async_relative_retry_no_payload)

        self.assertRaisesWithMessage("Operation failed",
            client.lrosa_ds.put_non_retry201_creating400_invalid_json, product)

if __name__ == '__main__':
    unittest.main()
