from Fields import Int32Field, ModelField, ArrayField, ConditionalField, ConditionalBlockStart, ConditionalBlockEnd
from Fields.Enums import EStorageType
from Func import ge
from Models import Model


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


class Grid(Model):
    itemId = Int32Field()
    filter = Int32Field()
    count = Int32Field()
    stackSize = Int32Field()


class StorageComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    versionCheckStart = ConditionalBlockStart(arg_fields='version', condition_func=ge(1))
    previous = Int32Field()
    next = Int32Field()
    bottom = Int32Field()
    top = Int32Field()
    versionCheckEnd = ConditionalBlockEnd()
    storageType = EStorageType()
    gridSize = Int32Field()
    bans = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(1))
    grids = ArrayField(lambda: ModelField(Grid), length_field='gridSize')
