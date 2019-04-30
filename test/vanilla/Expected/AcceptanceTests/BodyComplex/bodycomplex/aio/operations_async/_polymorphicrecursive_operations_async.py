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

from azure.core.exceptions import map_error

from ... import models


class PolymorphicrecursiveOperations:
    """PolymorphicrecursiveOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    async def get_valid(self, *, cls=None, **kwargs):
        """Get complex types that are polymorphic and have recursive references.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Fish or the result of cls(response)
        :rtype: ~bodycomplex.models.Fish
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Fish', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_valid.metadata = {'url': '/complex/polymorphicrecursive/valid'}

    async def put_valid(self, complex_body, *, cls=None, **kwargs):
        """Put complex types that are polymorphic and have recursive references.

        :param complex_body: Please put a salmon that looks like this:
         {
         "fishtype": "salmon",
         "species": "king",
         "length": 1,
         "age": 1,
         "location": "alaska",
         "iswild": true,
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "length": 20,
         "age": 6,
         "siblings": [
         {
         "fishtype": "salmon",
         "species": "coho",
         "length": 2,
         "age": 2,
         "location": "atlantic",
         "iswild": true,
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "length": 20,
         "age": 6
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "length": 10,
         "age": 105
         }
         ]
         }
        :type complex_body: ~bodycomplex.models.Fish
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_valid.metadata = {'url': '/complex/polymorphicrecursive/valid'}
