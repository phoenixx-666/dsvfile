from Field import Field
from lxml.etree import Element


class Reader(object):
    def __init__(self):
        self.field_values = {}

        cls = self.__class__
        fields = [(fname, field) for fname, field in cls.__dict__.items() if isinstance(field, Field)]
        fields.sort(key=lambda c: c[1].order)
        self._fields_ordered = fields
        self._hidden_fields = (fname for fname, field in fields if field.hidden)
        self._open_fields = (fname for fname, field in fields if not field.hidden)
        self._all_field_names = (fname for fname, field in fields)
        self.fields = {fname: field for fname, field in fields}
        self.skip_fields = False

    def read(self, input_stream):
        for fname, field in self._fields_ordered:
            val = field.read(input_stream, self)
            if fname in self._hidden_fields:
                continue
            self.field_values[fname] = val
        self.skip_fields = False

    def to_xml(self):
        cls_name = self.__class__.__name__
        cls_name = cls_name[0].upper() + cls_name[1:]
        xml = Element(cls_name)
        for fname, field in self._fields_ordered:
            child = field.to_xml(fname, self.field_values[fname], self)
            if self.skip_fields or fname in self._hidden_fields or child is None:
                continue
            xml.append(child)
        self.skip_fields = False
        return xml

    def __getattribute__(self, name):
        if name == 'field_values' or name not in self.field_values:
            return super(Reader, self).__getattribute__(name)
        return self.field_values[name]

    def __setattribute__(self, name, value):
        if name == 'field_values' or name not in self.field_values:
            super(Reader, self).__setattribute__(name, value)
        else:
            self.field_values[name] = value
