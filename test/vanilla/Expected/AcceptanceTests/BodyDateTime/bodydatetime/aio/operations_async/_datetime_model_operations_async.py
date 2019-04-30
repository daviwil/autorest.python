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


class DatetimeModelOperations:
    """DatetimeModelOperations async operations.

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

    async def get_null(self, *, cls=None, **kwargs):
        """Get null datetime value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_null.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_null.metadata = {'url': '/datetime/null'}

    async def get_invalid(self, *, cls=None, **kwargs):
        """Get invalid datetime value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_invalid.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_invalid.metadata = {'url': '/datetime/invalid'}

    async def get_overflow(self, *, cls=None, **kwargs):
        """Get overflow datetime value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_overflow.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_overflow.metadata = {'url': '/datetime/overflow'}

    async def get_underflow(self, *, cls=None, **kwargs):
        """Get underflow datetime value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_underflow.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_underflow.metadata = {'url': '/datetime/underflow'}

    async def put_utc_max_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put max datetime value 9999-12-31T23:59:59.9999999Z.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_utc_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_utc_max_date_time.metadata = {'url': '/datetime/max/utc'}

    async def get_utc_lowercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value 9999-12-31t23:59:59.9999999z.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_utc_lowercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_utc_lowercase_max_date_time.metadata = {'url': '/datetime/max/utc/lowercase'}

    async def get_utc_uppercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value 9999-12-31T23:59:59.9999999Z.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_utc_uppercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_utc_uppercase_max_date_time.metadata = {'url': '/datetime/max/utc/uppercase'}

    async def put_local_positive_offset_max_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put max datetime value with positive numoffset
        9999-12-31t23:59:59.9999999+14:00.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_local_positive_offset_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_local_positive_offset_max_date_time.metadata = {'url': '/datetime/max/localpositiveoffset'}

    async def get_local_positive_offset_lowercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value with positive num offset
        9999-12-31t23:59:59.9999999+14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_positive_offset_lowercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_positive_offset_lowercase_max_date_time.metadata = {'url': '/datetime/max/localpositiveoffset/lowercase'}

    async def get_local_positive_offset_uppercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value with positive num offset
        9999-12-31T23:59:59.9999999+14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_positive_offset_uppercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_positive_offset_uppercase_max_date_time.metadata = {'url': '/datetime/max/localpositiveoffset/uppercase'}

    async def put_local_negative_offset_max_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put max datetime value with positive numoffset
        9999-12-31t23:59:59.9999999-14:00.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_local_negative_offset_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_local_negative_offset_max_date_time.metadata = {'url': '/datetime/max/localnegativeoffset'}

    async def get_local_negative_offset_uppercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value with positive num offset
        9999-12-31T23:59:59.9999999-14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_negative_offset_uppercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_negative_offset_uppercase_max_date_time.metadata = {'url': '/datetime/max/localnegativeoffset/uppercase'}

    async def get_local_negative_offset_lowercase_max_date_time(self, *, cls=None, **kwargs):
        """Get max datetime value with positive num offset
        9999-12-31t23:59:59.9999999-14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_negative_offset_lowercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_negative_offset_lowercase_max_date_time.metadata = {'url': '/datetime/max/localnegativeoffset/lowercase'}

    async def put_utc_min_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put min datetime value 0001-01-01T00:00:00Z.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_utc_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_utc_min_date_time.metadata = {'url': '/datetime/min/utc'}

    async def get_utc_min_date_time(self, *, cls=None, **kwargs):
        """Get min datetime value 0001-01-01T00:00:00Z.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_utc_min_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_utc_min_date_time.metadata = {'url': '/datetime/min/utc'}

    async def put_local_positive_offset_min_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put min datetime value 0001-01-01T00:00:00+14:00.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_local_positive_offset_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_local_positive_offset_min_date_time.metadata = {'url': '/datetime/min/localpositiveoffset'}

    async def get_local_positive_offset_min_date_time(self, *, cls=None, **kwargs):
        """Get min datetime value 0001-01-01T00:00:00+14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_positive_offset_min_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_positive_offset_min_date_time.metadata = {'url': '/datetime/min/localpositiveoffset'}

    async def put_local_negative_offset_min_date_time(self, datetime_body, *, cls=None, **kwargs):
        """Put min datetime value 0001-01-01T00:00:00-14:00.

        :param datetime_body:
        :type datetime_body: datetime
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_local_negative_offset_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(datetime_body, 'iso-8601')

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
    put_local_negative_offset_min_date_time.metadata = {'url': '/datetime/min/localnegativeoffset'}

    async def get_local_negative_offset_min_date_time(self, *, cls=None, **kwargs):
        """Get min datetime value 0001-01-01T00:00:00-14:00.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: datetime or the result of cls(response)
        :rtype: datetime
        :raises: :class:`ErrorException<bodydatetime.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_local_negative_offset_min_date_time.metadata['url']

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
            deserialized = self._deserialize('iso-8601', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_local_negative_offset_min_date_time.metadata = {'url': '/datetime/min/localnegativeoffset'}
