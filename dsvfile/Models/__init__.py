from ..Fields import Field, Int32Field, ConditionalBlockStart, ConditionalBlockEnd


class Model(object):
    def __init__(self):
        self.field_values = {}

        fields = [(fname, field) for fname, field in self.__class__.__dict__.items() if isinstance(field, Field)]
        fields.sort(key=lambda c: c[1].order)
        self._fields_ordered = fields
        self._open_fields = tuple(fname for fname, field in fields if not field.hidden)
        self.fields = {fname: field for fname, field in fields}
        self.field_values = {fname: None for fname, field in fields if field.store_value}

    def read(self, input_stream):
        read_field = True
        for fname, field in self._fields_ordered:
            if not (read_field or field.always_read):
                continue
            if isinstance(field, ConditionalBlockStart):
                read_field = field.read(input_stream, self)
            elif isinstance(field, ConditionalBlockEnd):
                read_field = True
            elif field.store_value:
                self.field_values[fname] = field.read(input_stream, self)

    def __getattribute__(self, name):
        if name == 'field_values' or name not in self.field_values:
            return super(Model, self).__getattribute__(name)
        return self.field_values[name]

    def __setattribute__(self, name, value):
        if name == 'field_values' or name not in self.field_values:
            super(Model, self).__setattribute__(name, value)
        else:
            self.field_values[name] = value

    @property
    def field_list(self):
        return self._open_fields


class Int32KVP(Model):
    key = Int32Field()
    value = Int32Field()
