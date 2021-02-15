from Field import Int32Field
from Reader import Reader


class GalacticTransport(Reader):
    version = Int32Field()
