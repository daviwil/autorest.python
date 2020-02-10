# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class QueriesOperations(object):
    """QueriesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~urlmulticollectionformat.models
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
    def array_string_multi_null(
        self,
        array_query=None,  # type: Optional[List[str]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get a null array of string using the multi-array format.

        :param array_query: a null array of string using the multi-array format.
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.array_string_multi_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    array_string_multi_null.metadata = {'url': '/queries/array/multi/string/null'}

    @distributed_trace
    def array_string_multi_empty(
        self,
        array_query=None,  # type: Optional[List[str]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an empty array [] of string using the multi-array format.

        :param array_query: an empty array [] of string using the multi-array format.
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.array_string_multi_empty.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    array_string_multi_empty.metadata = {'url': '/queries/array/multi/string/empty'}

    @distributed_trace
    def array_string_multi_valid(
        self,
        array_query=None,  # type: Optional[List[str]]
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' , null, ''] using the mult-array format.

        :param array_query: an empty array [] of string using the multi-array format.
        :type array_query: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.array_string_multi_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    array_string_multi_valid.metadata = {'url': '/queries/array/multi/string/valid'}
