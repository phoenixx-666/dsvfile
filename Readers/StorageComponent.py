from Field import Int32Field, EnumField, ReaderField, ArrayField
from Reader import Reader

"""
StorageComponent
{
    int32 version = 1
    int32 id
    int32 entityId
    int32 previous (version >= 1)
    int32 next (version >= 1)
    int32 bottom (version >= 1)
    int32 top (version >= 1)
    int32 EStorageType type (0:Default 1:Fuel 9:Filtered)
    int32 gridSize
    int32 bans (version >= 1)
    grids[gridSize] {
        int32 itemId
        int32 filter
        int32 count
        int32 stackSize
    }
}
"""


class EStorageType(EnumField):
    enum_values = {
        0: 'Default',
        1: 'Fuel',
        9: 'Filtered'
    }


class Grid(Reader):
    itemId = Int32Field()
    filter = Int32Field()
    count = Int32Field()
    stackSize = Int32Field()


class StorageComponent(Reader):
    version = Int32Field()
    scId = Int32Field()
    entityId = Int32Field()
    previous = Int32Field()
    next = Int32Field()
    bottom = Int32Field()
    top = Int32Field()
    storageType = EStorageType()
    gridSize = Int32Field()
    bans = Int32Field()
    grids = ArrayField(lambda: ReaderField(Grid), length_field='gridSize')
