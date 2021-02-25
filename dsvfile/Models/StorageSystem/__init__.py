from ...Fields import ModelField, ArrayField, ConditionalField
from ...Func import ne, decr
from .. import Model, Int32Field
from .StorageComponent import StorageComponent
from .TankComponent import TankComponent


class StorageSwitch(Model):
    storagePoolIndex = Int32Field()
    size = ConditionalField(Int32Field, arg_fields='storagePoolIndex', condition_func=ne(0))
    storagePool = ConditionalField(ModelField(StorageComponent), arg_fields='storagePoolIndex', condition_func=ne(0))


class FactoryStorage(Model):
    version = Int32Field()
    storageCursor = Int32Field()
    storageCapacity = Int32Field()
    storageRecycleCursor = Int32Field()
    storagePool = ArrayField(ModelField(StorageSwitch), length_field='storageCursor', length_func=decr())
    storageRecycle = ArrayField(Int32Field, length_field='storageRecycleCursor')
    tankCapacity = Int32Field()
    tankCursor = Int32Field()
    tankRecycleCursor = Int32Field()
    tankPool = ArrayField(ModelField(TankComponent), length_field='tankCursor', length_func=decr())
    tankRecycle = ArrayField(Int32Field, length_field='tankRecycleCursor')
