from Field import Int32Field, UInt32Field, ByteStringField, ArrayField
from Reader import Reader


"""
PlatformSystem
{
    int32 version = 0
    int32 reformDataByteCount
    uint8 reformData[reformDataByteCount]: If count exceeds a limit, count is read, but only the limit is used.
    int32 reformOffsetsByteCount
    uint32 reformOffsets[reformOffsetsByteCount]: If count exceeds a limit, count is read, but only the limit is used.
}
"""


class PlatformSystem(Reader):
    version = Int32Field()
    reformData = ByteStringField()
    reformOffsets = ArrayField(UInt32Field)
