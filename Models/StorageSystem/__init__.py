from Fields import Int32Field, ModelField, ArrayField, ConditionalField
from Func import ne, decr
from Models import Model
from Models.StorageSystem.StorageComponent import StorageComponent
from Models.StorageSystem.TankComponent import TankComponent


"""
FactoryStorage
{
    int32 version = 0
    int32 storageCursor
    int32 storageCapacity
    int32 storageRecycleCursor
    [storageCursor - 1] {
        int32 storagePoolIndex
        int32 size (storagePoolIndex != 0)
        StorageComponent storagePool (storagePoolIndex != 0)
    }
    int32 storageRecycle[storageRecycleCursor]
    int32 tankCapacity
    int32 tankCursor
    int32 tankRecycleCursor
    TankComponent tankPool[tankCursor]
    int32 tankRecycle[tankRecycleCursor]
}
"""


class StorageSwitch(Model):
    storagePoolIndex = Int32Field()
    size = ConditionalField(Int32Field, arg_fields='storagePoolIndex', condition_func=ne(0))
    storagePool = ConditionalField(lambda: ModelField(StorageComponent), arg_fields='storagePoolIndex', condition_func=ne(0))


class FactoryStorage(Model):
    version = Int32Field()
    storageCursor = Int32Field()
    storageCapacity = Int32Field()
    storageRecycleCursor = Int32Field()
    storagePool = ArrayField(lambda: ModelField(StorageSwitch), length_field='storageCursor', length_func=decr())
    storageRecycle = ArrayField(Int32Field, length_field='storageRecycleCursor')
    tankCapacity = Int32Field()
    tankCursor = Int32Field()
    tankRecycleCursor = Int32Field()
    tankPool = ArrayField(lambda: ModelField(TankComponent), length_field='tankCursor', length_func=decr())
    tankRecycle = ArrayField(Int32Field, length_field='tankRecycleCursor')
