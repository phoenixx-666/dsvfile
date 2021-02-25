from ..Fields import Field, FieldMap, Int32Field, ConditionalBlockStart, ConditionalBlockEnd


__all__ = ['Model', 'Int32KVP']


class Model(object):
    _field_values = {}

    def __init__(self):
        fields = {fname: field for fname, field in self.__class__.__dict__.items() if isinstance(field, Field)}
        ordered_fields = sorted(((fname, field) for fname, field in fields.items()),
                                key=lambda c: c[1].initialization_order)
        self._ordered_fields = ordered_fields
        self._fields = FieldMap(fields)
        self._open_fields = tuple(fname for fname, field in ordered_fields if not field.hidden)
        self._field_values = {fname: None for fname, field in ordered_fields if field.store_value}

    def read(self, input_stream):
        read_field = True
        for fname, field in self._ordered_fields:
            if not (read_field or field.always_read):
                continue
            if isinstance(field, ConditionalBlockStart):
                read_field = field.read(None, self)
            elif isinstance(field, ConditionalBlockEnd):
                read_field = True
            elif field.store_value:
                self._field_values[fname] = field.read(input_stream, self)

    def write(self, output_stream):
        write_field = True
        for fname, field in self._ordered_fields:
            if not (write_field or field.always_read):
                continue
            if isinstance(field, ConditionalBlockStart):
                write_field = field.read(None, self)
            elif isinstance(field, ConditionalBlockEnd):
                write_field = True
            elif field.write_value:
                field.write(self._field_values[fname], output_stream, self)

    def __getattribute__(self, name):
        if name != '_field_values' and name in self._field_values:
            return self._field_values[name]
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name != '_field_values' and name in self._field_values:
            self._field_values[name] = value
        else:
            super().__setattr__(name, value)

    @property
    def field_list(self):
        return self._open_fields

    @property
    def fields(self):
        return self._fields


class Int32KVP(Model):
    key = Int32Field()
    value = Int32Field()
