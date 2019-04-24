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


class ChildProduct(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Required. Constant string. Default value: "constant"
     .
    :vartype const_property: str
    :param count: Count
    :type count: int
    """

    _validation = {
        'const_property': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    const_property = "constant"

    def __init__(self, *, count: int=None, **kwargs) -> None:
        super(ChildProduct, self).__init__(**kwargs)
        self.count = count


class ConstantProduct(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Required. Constant string. Default value: "constant"
     .
    :vartype const_property: str
    :ivar const_property2: Required. Constant string2. Default value:
     "constant2" .
    :vartype const_property2: str
    """

    _validation = {
        'const_property': {'required': True, 'constant': True},
        'const_property2': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'const_property2': {'key': 'constProperty2', 'type': 'str'},
    }

    const_property = "constant"

    const_property2 = "constant2"


class Error(Model):
    """Error.

    :param code:
    :type code: int
    :param message:
    :type message: str
    :param fields:
    :type fields: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'fields': {'key': 'fields', 'type': 'str'},
    }

    def __init__(self, *, code: int=None, message: str=None, fields: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.fields = fields


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


class Product(Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param display_names: Non required array of unique items from 0 to 6
     elements.
    :type display_names: list[str]
    :param capacity: Non required int betwen 0 and 100 exclusive.
    :type capacity: int
    :param image: Image URL representing the product.
    :type image: str
    :param child: Required.
    :type child: ~validation.models.ChildProduct
    :ivar const_child: Required.
    :vartype const_child: ~validation.models.ConstantProduct
    :ivar const_int: Required. Constant int. Default value: 0 .
    :vartype const_int: int
    :ivar const_string: Required. Constant string. Default value: "constant" .
    :vartype const_string: str
    :param const_string_as_enum: Constant string as Enum. Possible values
     include: 'constant_string_as_enum'
    :type const_string_as_enum: str or ~validation.models.EnumConst
    """

    _validation = {
        'display_names': {'max_items': 6, 'min_items': 0, 'unique': True},
        'capacity': {'maximum_ex': 100, 'minimum_ex': 0},
        'image': {'pattern': r'http://\w+'},
        'child': {'required': True},
        'const_child': {'required': True, 'constant': True},
        'const_int': {'required': True, 'constant': True},
        'const_string': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'display_names': {'key': 'display_names', 'type': '[str]'},
        'capacity': {'key': 'capacity', 'type': 'int'},
        'image': {'key': 'image', 'type': 'str'},
        'child': {'key': 'child', 'type': 'ChildProduct'},
        'const_child': {'key': 'constChild', 'type': 'ConstantProduct'},
        'const_int': {'key': 'constInt', 'type': 'int'},
        'const_string': {'key': 'constString', 'type': 'str'},
        'const_string_as_enum': {'key': 'constStringAsEnum', 'type': 'EnumConst'},
    }

    const_child = ConstantProduct()

    const_int = 0

    const_string = "constant"

    def __init__(self, *, child, display_names=None, capacity: int=None, image: str=None, const_string_as_enum=None, **kwargs) -> None:
        super(Product, self).__init__(**kwargs)
        self.display_names = display_names
        self.capacity = capacity
        self.image = image
        self.child = child
        self.const_string_as_enum = const_string_as_enum
