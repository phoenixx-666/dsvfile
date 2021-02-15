from Field import Int32Field
from Reader import Reader


class Int32KVP(Reader):
    key = Int32Field()
    value = Int32Field()
