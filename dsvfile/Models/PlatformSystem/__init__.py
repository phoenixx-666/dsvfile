from ...Fields import UInt32Field, ByteStringField, ArrayField
from .. import Model, Int32Field


class PlatformSystem(Model):
    version = Int32Field()
    reformData = ByteStringField()
    reformOffsets = ArrayField(UInt32Field)
