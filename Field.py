import numpy as np
from lxml.etree import Element


class IncorrectHeaderException(IOError):
    pass


class Field(object):
    field_counter = 0
    type_name = None

    def __init__(self):
        cls = self.__class__
        self.order = Field.field_counter
        Field.field_counter += 1

    def read(self, input_stream, reader):
        raise NotImplementedError

    def visualize(self, value):
        return '{}'.format(value)

    def to_xml(self, name, value, reader):
        elem = Element(name, type=self.type_name)
        elem.text = self.visualize(value)
        return elem


class FixedHeaderField(Field):
    type_name = 'header'

    def __init__(self, header):
        self.header = header
        super().__init__()
    
    def read(self, input_stream, reader):
        if input_stream.read(len(self.header)).decode('ISO 8859-1') != self.header:
            raise IncorrectHeaderException
        return self.header


class FixedSizeNumberField(Field):
    size = None
    dtype = None

    def read(self, input_stream, reader):
        cls = self.__class__
        return np.frombuffer(input_stream.read(cls.size), dtype=cls.dtype)[0]


class UInt8Field(FixedSizeNumberField):
    type_name = 'uint8'
    size = 1
    dtype = np.uint8


class Int32Field(FixedSizeNumberField):
    type_name = 'int32'
    size = 4
    dtype = np.int32


class Int64Field(FixedSizeNumberField):
    type_name = 'int64'
    size = 8
    dtype = np.int64


class FloatField(FixedSizeNumberField):
    type_name = 'float'
    size = 4
    dtype = np.float32


class DoubleField(FixedSizeNumberField):
    type_name = 'double'
    size = 8
    dtype = np.double


class EnumField(Field):
    type_name = 'enum'
    enum_values = {}
    base_type = Int32Field

    def __init__(self):
        self.field = self.base_type()
        if isinstance(self.enum_values, dict):
            self.enum_values = self.enum_values
        elif isinstance(self.enum_values, (tuple, list)):
            self.enum_values = {i: v for i, v in enumerate(self.enum_values)}
        else:
            raise TypeError()
        super().__init__()

    def read(self, input_stream, reader):
        return self.field.read(input_stream, reader)

    def to_xml(self, name, value, reader):
        elem = Element(name, type=self.type_name, attrib={
            'base-value': str(value),
            'base-type': self.field.type_name
        })
        elem.text = self.enum_values.get(value, str(value))
        return elem


class StringField(Field):
    type_name = 'string'

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
        super().__init__()

    def read(self, input_stream, reader):
        length = input_stream.read(1)[0]
        return input_stream.read(length).decode('utf-8')

    def visualize(self, value):
        if len(value) > 50:
            return '{}...'.format(value[:50])
        return value


class ByteStringField(Field):
    type_name = 'bytestring'

    def __init__(self, length_field=Int32Field):
        self.length_field = length_field()
        super().__init__()
    
    def read(self, input_stream, reader):
        length = self.length_field.read(input_stream, reader)
        return input_stream.read(length)

    def visualize(self, value):
        # if len(value) > 50:
        #     return '{}...'.format(value[:50])
        # return super(ByteArrayField, self).visualize(value)
        return 'Binary data'


class ArrayField(Field):
    type_name = 'array'

    def __init__(self, item_field, length_field=Int32Field, length_function=None):
        self.item_field = item_field()
        if isinstance(length_field, str):
            self.length_field = length_field
        else:
            self.length_field = length_field()
        self.length_function = length_function
        super().__init__()

    def read(self, input_stream, reader):
        if isinstance(self.length_field, str):
            length = reader.__getattribute__(self.length_field)
        else:
            length = self.length_field.read(input_stream, reader)
        if self.length_function is not None:
            length = self.length_function(length)
        return [self.item_field.read(input_stream, reader) for i in range(length)]

    def visualize(self, value):
        return value

    def to_xml(self, name, value, reader):
        if isinstance(self.length_field, str):
            length_type = reader.fields[name].type_name
        else:
            length_type = self.length_field.type_name
        elem = Element(name, type=self.type_name, attrib={
            'length': str(len(value)),
            'item-type': self.item_field.type_name,
            'length-type': length_type
        })
        for item in value:
            elem.append(self.item_field.to_xml('ArrayItem', item, reader))
        return elem


class ReaderField(Field):
    type_name = 'struct'

    def __init__(self, reader_class):
        self.reader_class = reader_class
        super().__init__()
    
    def read(self, input_stream, reader):
        local_reader = self.reader_class()
        local_reader.read(input_stream)
        return local_reader

    def visualize(self, value):
        return value

    def to_xml(self, name, value, reader):
        return value.to_xml()
