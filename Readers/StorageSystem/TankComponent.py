from Field import Int32Field, BoolField
from Reader import Reader


"""
TankComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 lastTankId
    int32 nextTankId
    int32 belt0
    int32 belt1
    int32 belt2
    int32 belt3
    uint8_bool isOutput0
    uint8_bool isOutput1
    uint8_bool isOutput2
    uint8_bool isOutput3
    int32 fluidStorageCount
    int32 currentCount
    int32 fluidId
    uint8_bool outputSwitch
    uint8_bool inputSwitch
    uint8_bool isBottom
}
"""


class TankComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    lastTankId = Int32Field()
    nextTankId = Int32Field()
    belt0 = Int32Field()
    belt1 = Int32Field()
    belt2 = Int32Field()
    belt3 = Int32Field()
    isOutput0 = BoolField()
    isOutput1 = BoolField()
    isOutput2 = BoolField()
    isOutput3 = BoolField()
    fluidStorageCount = Int32Field()
    currentCount = Int32Field()
    fluidId = Int32Field()
    outputSwitch = BoolField()
    inputSwitch = BoolField()
    isBottom = BoolField()
