from Field import Int32Field, ReaderField, ArrayField, ConditionalField
from Func import ne, decr
from Reader import Reader
from Readers.StorageSystem.StorageComponent import StorageComponent
from Readers.StorageSystem.TankComponent import TankComponent


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


class StorageSwitch(Reader):
    storagePoolIndex = Int32Field()
    size = ConditionalField(Int32Field, arg_fields='storagePoolIndex', condition_func=ne(0))
    storagePool = ConditionalField(lambda: ReaderField(StorageComponent), arg_fields='storagePoolIndex', condition_func=ne(0))


class FactoryStorage(Reader):
    version = Int32Field()
    storageCursor = Int32Field()
    storageCapacity = Int32Field()
    storageRecycleCursor = Int32Field()
    storagePool = ArrayField(lambda: ReaderField(StorageSwitch), length_field='storageCursor', condition_func=decr())
    storageRecycle = ArrayField(Int32Field, length_field='storageRecycleCursor')

    tankCapacity = Int32Field()
    tankCursor = Int32Field()
    tankRecycleCursor = Int32Field()
    tankPool = ArrayField(lambda: ReaderField(TankComponent), length_field='tankCursor')
    tankRecycle = ArrayField(Int32Field, length_field='tankRecycleCursor')
