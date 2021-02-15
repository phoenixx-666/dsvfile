from Field import Field
from lxml.etree import Element


class Reader(object):
    def __init__(self):
        self.field_values = {}

        cls = self.__class__
        fields = [(fname, field) for fname, field in cls.__dict__.items() if isinstance(field, Field)]
        fields.sort(key=lambda c: c[1].order)
        self.fields_ordered = fields
        self.field_names = [fname for fname, field in fields]
        self.fields = {fname: field for fname, field in fields}

    def read(self, input_stream):
        for fname, field in self.fields_ordered:
            self.field_values[fname] = field.read(input_stream, self)

    def to_xml(self):
        """def to_nodes(fname, val):
            fname = fname[0].upper() + fname[1:]
            if isinstance(val, list):
                elem = Element(fname)
                for item in val:
                    elem.append(to_nodes('ArrayItem', item))
            elif isinstance(val, Reader):
                elem = val.to_xml()
            else:
                elem = Element(fname)
                elem.text = val
            return elem"""

        cls_name = self.__class__.__name__
        cls_name = cls_name[0].upper() + cls_name[1:]
        xml = Element(cls_name)
        for fname, field in self.fields_ordered:
            xml.append(field.to_xml(fname, self.field_values[fname], self))
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
