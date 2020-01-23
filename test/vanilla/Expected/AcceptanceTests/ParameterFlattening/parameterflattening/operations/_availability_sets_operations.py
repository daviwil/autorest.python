# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.tracing.decorator import distributed_trace

from .. import models


class AvailabilitySetsOperations(object):
    """AvailabilitySetsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~parameterflattening.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def update(self, resource_group_name, avset, availability_set_update_parameters_tags, cls=None, **kwargs):
        """Updates the tags for an availability set.

        FIXME: add operation.summary

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param avset: The name of the storage availability set.
        :type avset: str
        :param availability_set_update_parameters_tags: A description about the set of tags.
        :type availability_set_update_parameters_tags: dict[str, str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        tags = models.AvailabilitySetUpdateParameters(availability_set_update_parameters_tags=availability_set_update_parameters_tags)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'availabilitySetName': self._serialize.url("avset", avset, 'str', max_length=80, min_length=0),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(tags, 'AvailabilitySetUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(response, None, {})

    update.metadata = {'url': '/parameterFlattening/{resourceGroupName}/{availabilitySetName}'}
