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

from msrest.serialization import Model
from azure.core import HttpRequestError


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class ErrorException(HttpRequestError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

      model_name = 'Error'
      self.error = deserialize(model_name, response)
      if self.error is None:
          self.error = deserialize.dependencies[model_name]()
      super(ErrorException, self).__init__(response=response)


class FirstParameterGroup(Model):
    """Additional parameters for a set of operations, such as:
    ParameterGrouping_post_multi_param_groups,
    ParameterGrouping_post_shared_parameter_group_object.

    :param header_one:
    :type header_one: str
    :param query_one: Query parameter with default. Default value: 30 .
    :type query_one: int
    """

    _attribute_map = {
        'header_one': {'key': '', 'type': 'str'},
        'query_one': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, header_one: str=None, query_one: int=30, **kwargs) -> None:
        super(FirstParameterGroup, self).__init__(**kwargs)
        self.header_one = header_one
        self.query_one = query_one


class HttpRequestError(Model):
    """HttpRequestError.
    """

    _attribute_map = {
    }


class ParameterGroupingPostMultiParamGroupsSecondParamGroup(Model):
    """Additional parameters for post_multi_param_groups operation.

    :param header_two:
    :type header_two: str
    :param query_two: Query parameter with default. Default value: 30 .
    :type query_two: int
    """

    _attribute_map = {
        'header_two': {'key': '', 'type': 'str'},
        'query_two': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, header_two: str=None, query_two: int=30, **kwargs) -> None:
        super(ParameterGroupingPostMultiParamGroupsSecondParamGroup, self).__init__(**kwargs)
        self.header_two = header_two
        self.query_two = query_two


class ParameterGroupingPostOptionalParameters(Model):
    """Additional parameters for post_optional operation.

    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default. Default value: 30 .
    :type query: int
    """

    _attribute_map = {
        'custom_header': {'key': '', 'type': 'str'},
        'query': {'key': '', 'type': 'int'},
    }

    def __init__(self, *, custom_header: str=None, query: int=30, **kwargs) -> None:
        super(ParameterGroupingPostOptionalParameters, self).__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query


class ParameterGroupingPostRequiredParameters(Model):
    """Additional parameters for post_required operation.

    All required parameters must be populated in order to send to Azure.

    :param body: Required.
    :type body: int
    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default. Default value: 30 .
    :type query: int
    :param path: Required. Path parameter
    :type path: str
    """

    _validation = {
        'body': {'required': True},
        'path': {'required': True},
    }

    _attribute_map = {
        'body': {'key': '', 'type': 'int'},
        'custom_header': {'key': '', 'type': 'str'},
        'query': {'key': '', 'type': 'int'},
        'path': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, body: int, path: str, custom_header: str=None, query: int=30, **kwargs) -> None:
        super(ParameterGroupingPostRequiredParameters, self).__init__(**kwargs)
        self.body = body
        self.custom_header = custom_header
        self.query = query
        self.path = path
