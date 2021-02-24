from ..Fields import Field, Int32Field, ConditionalBlockStart, ConditionalBlockEnd


class Model(object):
    def __init__(self):
        self.field_values = {}

        ordered_fields = [(fname, field) for fname, field in self.__class__.__dict__.items()
                          if isinstance(field, Field)]
        ordered_fields.sort(key=lambda c: c[1].order)
        self._ordered_fields = ordered_fields
        self._open_fields = tuple(fname for fname, field in ordered_fields if not field.hidden)
        self.fields = {fname: field for fname, field in ordered_fields}
        self.field_values = {fname: None for fname, field in ordered_fields if field.store_value}

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
                self.field_values[fname] = field.read(input_stream, self)

    def write(self, output_stream):
        write_field = True
        for fname, field in self._ordered_fields:
            if not (write_field or field.always_read):
                continue
            if isinstance(field, ConditionalBlockStart):
                write_field = field.read(None, self)
            elif isinstance(field, ConditionalBlockEnd):
                write_field = True
            elif field.store_value and not field.hidden:
                field.write(self.field_values[fname], output_stream, self)

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
