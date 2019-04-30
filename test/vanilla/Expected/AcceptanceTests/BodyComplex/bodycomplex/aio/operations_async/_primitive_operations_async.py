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


class PrimitiveOperations:
    """PrimitiveOperations async operations.

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

    async def get_int(self, *, cls=None, **kwargs):
        """Get complex types with integer properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: IntWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.IntWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_int.metadata['url']

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
            deserialized = self._deserialize('IntWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_int.metadata = {'url': '/complex/primitive/integer'}

    async def put_int(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with integer properties.

        :param complex_body: Please put -1 and 2
        :type complex_body: ~bodycomplex.models.IntWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_int.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'IntWrapper')

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
    put_int.metadata = {'url': '/complex/primitive/integer'}

    async def get_long(self, *, cls=None, **kwargs):
        """Get complex types with long properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: LongWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.LongWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_long.metadata['url']

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
            deserialized = self._deserialize('LongWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_long.metadata = {'url': '/complex/primitive/long'}

    async def put_long(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with long properties.

        :param complex_body: Please put 1099511627775 and -999511627788
        :type complex_body: ~bodycomplex.models.LongWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'LongWrapper')

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
    put_long.metadata = {'url': '/complex/primitive/long'}

    async def get_float(self, *, cls=None, **kwargs):
        """Get complex types with float properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: FloatWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.FloatWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_float.metadata['url']

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
            deserialized = self._deserialize('FloatWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_float.metadata = {'url': '/complex/primitive/float'}

    async def put_float(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with float properties.

        :param complex_body: Please put 1.05 and -0.003
        :type complex_body: ~bodycomplex.models.FloatWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'FloatWrapper')

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
    put_float.metadata = {'url': '/complex/primitive/float'}

    async def get_double(self, *, cls=None, **kwargs):
        """Get complex types with double properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: DoubleWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DoubleWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_double.metadata['url']

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
            deserialized = self._deserialize('DoubleWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_double.metadata = {'url': '/complex/primitive/double'}

    async def put_double(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with double properties.

        :param complex_body: Please put 3e-100 and
         -0.000000000000000000000000000000000000000000000000000000005
        :type complex_body: ~bodycomplex.models.DoubleWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DoubleWrapper')

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
    put_double.metadata = {'url': '/complex/primitive/double'}

    async def get_bool(self, *, cls=None, **kwargs):
        """Get complex types with bool properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: BooleanWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.BooleanWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_bool.metadata['url']

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
            deserialized = self._deserialize('BooleanWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_bool.metadata = {'url': '/complex/primitive/bool'}

    async def put_bool(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with bool properties.

        :param complex_body: Please put true and false
        :type complex_body: ~bodycomplex.models.BooleanWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'BooleanWrapper')

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
    put_bool.metadata = {'url': '/complex/primitive/bool'}

    async def get_string(self, *, cls=None, **kwargs):
        """Get complex types with string properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: StringWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.StringWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_string.metadata['url']

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
            deserialized = self._deserialize('StringWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_string.metadata = {'url': '/complex/primitive/string'}

    async def put_string(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with string properties.

        :param complex_body: Please put 'goodrequest', '', and null
        :type complex_body: ~bodycomplex.models.StringWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'StringWrapper')

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
    put_string.metadata = {'url': '/complex/primitive/string'}

    async def get_date(self, *, cls=None, **kwargs):
        """Get complex types with date properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: DateWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DateWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_date.metadata['url']

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
            deserialized = self._deserialize('DateWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_date.metadata = {'url': '/complex/primitive/date'}

    async def put_date(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with date properties.

        :param complex_body: Please put '0001-01-01' and '2016-02-29'
        :type complex_body: ~bodycomplex.models.DateWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DateWrapper')

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
    put_date.metadata = {'url': '/complex/primitive/date'}

    async def get_date_time(self, *, cls=None, **kwargs):
        """Get complex types with datetime properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: DatetimeWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DatetimeWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_date_time.metadata['url']

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
            deserialized = self._deserialize('DatetimeWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_date_time.metadata = {'url': '/complex/primitive/datetime'}

    async def put_date_time(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with datetime properties.

        :param complex_body: Please put '0001-01-01T12:00:00-04:00' and
         '2015-05-18T11:38:00-08:00'
        :type complex_body: ~bodycomplex.models.DatetimeWrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DatetimeWrapper')

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
    put_date_time.metadata = {'url': '/complex/primitive/datetime'}

    async def get_date_time_rfc1123(self, *, cls=None, **kwargs):
        """Get complex types with datetimeRfc1123 properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Datetimerfc1123Wrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.Datetimerfc1123Wrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_date_time_rfc1123.metadata['url']

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
            deserialized = self._deserialize('Datetimerfc1123Wrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    async def put_date_time_rfc1123(self, complex_body, *, cls=None, **kwargs):
        """Put complex types with datetimeRfc1123 properties.

        :param complex_body: Please put 'Mon, 01 Jan 0001 12:00:00 GMT' and
         'Mon, 18 May 2015 11:38:00 GMT'
        :type complex_body: ~bodycomplex.models.Datetimerfc1123Wrapper
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.put_date_time_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Datetimerfc1123Wrapper')

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
    put_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    async def get_duration(self, *, cls=None, **kwargs):
        """Get complex types with duration properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: DurationWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DurationWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_duration.metadata['url']

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
            deserialized = self._deserialize('DurationWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_duration.metadata = {'url': '/complex/primitive/duration'}

    async def put_duration(self, field=None, *, cls=None, **kwargs):
        """Put complex types with duration properties.

        :param field:
        :type field: timedelta
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        complex_body = models.DurationWrapper(field=field)

        # Construct URL
        url = self.put_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DurationWrapper')

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
    put_duration.metadata = {'url': '/complex/primitive/duration'}

    async def get_byte(self, *, cls=None, **kwargs):
        """Get complex types with byte properties.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: ByteWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.ByteWrapper
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_byte.metadata['url']

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
            deserialized = self._deserialize('ByteWrapper', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_byte.metadata = {'url': '/complex/primitive/byte'}

    async def put_byte(self, field=None, *, cls=None, **kwargs):
        """Put complex types with byte properties.

        :param field:
        :type field: bytearray
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        complex_body = models.ByteWrapper(field=field)

        # Construct URL
        url = self.put_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'ByteWrapper')

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
    put_byte.metadata = {'url': '/complex/primitive/byte'}
