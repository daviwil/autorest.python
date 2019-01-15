# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.async_client import SDKClientAsync
from msrest import Serializer, Deserializer

from ._configuration import AutoRestHeadTestServiceConfiguration
from .operations_async import HttpSuccessOperations


class AutoRestHeadTestServiceAsync(SDKClientAsync):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestHeadTestServiceConfiguration

    :ivar http_success: HttpSuccess operations
    :vartype http_success: head.operations.HttpSuccessOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AutoRestHeadTestServiceConfiguration(credentials, base_url)
        super(AutoRestHeadTestServiceAsync, self).__init__(self.config)

        client_models = {}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.http_success = HttpSuccessOperations(
            self._client, self.config, self._serialize, self._deserialize)