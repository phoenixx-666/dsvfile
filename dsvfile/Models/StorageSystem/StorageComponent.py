from ...Fields import ConditionalBlockStart, ConditionalBlockEnd
from ...Fields.Enums import EItem, EStorageType
from ...Func import ge
from . import Model, Int32Field, ModelField, ArrayField, ConditionalField


class Grid(Model):
    itemId = EItem()
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
    grids = ArrayField(ModelField(Grid), length_field='gridSize')
