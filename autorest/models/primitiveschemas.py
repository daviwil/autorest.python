from enum import Enum
from .baseschema import BaseSchema
from ..common.utils import to_python_type

class PrimitiveSchema(BaseSchema):
    def __init__(self, name, description, schema_type, **kwargs):
        super(PrimitiveSchema, self).__init__(name, description, **kwargs)
        self.schema_type = to_python_type(schema_type)

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, required):
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type=schema_type,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant']
        )


class NumberSchema(PrimitiveSchema):
    def __init__(self, name, description, schema_type, **kwargs):
        super(NumberSchema, self).__init__(name, description, schema_type)
        self.precision = kwargs.pop('precision', None)
        self.multiple_of = kwargs.pop('multiple_of', None)
        self.maximum = kwargs.pop('maximum', None)
        self.minimum = kwargs.pop('minimum', None)
        self.exclusive_maximum = kwargs.pop('exclusive_maximum', None)
        self.exclusive_minimum = kwargs.pop('exclusive_minimum', None)

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, required):
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type=schema_type,
            precision=yaml_data.get('precision'),
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            multiple_of = yaml_data.get('multipleOf'),
            maximum=yaml_data.get('maximum'),
            minimum=yaml_data.get('minimum'),
            exclusive_maximum=yaml_data.get('exclusiveMaximum'),
            exclusive_minimum=yaml_data.get('exclusiveMinimum')
        )

class StringSchema(PrimitiveSchema):
    def __init__(self, name, description, schema_type, **kwargs):
        super(StringSchema, self).__init__(name, description, schema_type)
        self.max_length = kwargs.pop('max_length', None)
        self.min_length = kwargs.pop('min_length', None)
        self.pattern = kwargs.pop('pattern', None)

    @classmethod
    def from_yaml(cls, name, yaml_data, required):
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type='string',
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
            max_length=yaml_data.get('maxLength'),
            min_length=yaml_data.get('minLength'),
            pattern=yaml_data.get('pattern')
        )
    

class DatetimeSchema(PrimitiveSchema):
    def __init__(self, name, description, schema_type, **kwargs):
        super(DatetimeSchema, self).__init__(name, description, schema_type, kwargs)
        self.format = kwargs.pop(format, None)

    class Formats(str, Enum):
        datetime = "date-time"
        rfc1123 = "date-time-rfc1123"

    @classmethod
    def from_yaml(cls, name, yaml_data, schema_type, required):
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type=schema_type,
            format=cls.Formats(yaml_data['format']) if yaml_data.get('format') else None,
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
        )


class ByteArraySchema(PrimitiveSchema):
    def __init__(self, name, description, schema_type, format, **kwargs):
        super(ByteArraySchema, self).__init__(name, description, schema_type, kwargs)
        self.format = format

    class Formats(str, Enum):
        base64url = "base64url"
        byte = "byte"

    @classmethod
    def from_yaml(cls, name, yaml_data, required):
        common_parameters_dict = cls._get_common_parameters(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
        return cls(
            name=name,
            description=common_parameters_dict['description'],
            schema_type='byte-array',
            format=cls.Formats(yaml_data['format']),
            required=common_parameters_dict['required'],
            readonly=common_parameters_dict['readonly'],
            constant=common_parameters_dict['constant'],
        )

def get_primitive_schema(name, yaml_data, schema_type, required):
    if schema_type in ('integer', 'number'):
        return NumberSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            schema_type=schema_type,
            required=required
        )
    if schema_type == 'string':
        return StringSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    if schema_type in ('date', 'date-time', 'unixtime'):
        return DatetimeSchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            schema_type=schema_type,
            required=required
        )
    if schema_type  == 'byte-array':
        return ByteArraySchema.from_yaml(
            name=name,
            yaml_data=yaml_data,
            required=required
        )
    return PrimitiveSchema.from_yaml(
        name=name,
        yaml_data=yaml_data,
        schema_type=schema_type,
        required=required
    )