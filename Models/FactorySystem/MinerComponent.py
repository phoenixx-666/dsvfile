from Fields import Int32Field, UInt32Field, ArrayField
from Fields.Enums import EMinerType, EWorkState
from Models import Model


"""
MinerComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 pcId
    int32 EMinerType type (None, Water, Vein, Oil)
    int32 speed
    int32 time
    int32 period
    int32 insertTarget
    int32 EWorkState workstate (Idle, Running, Outputing, Lack, Full)
    int32 veinCount
    int32 veins[veinCount]
    int32 currentVeinIndex
    int32 minimumVeinAmount
    int32 productId
    int32 productCount
    uint32 seed
}
"""


class MinerComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    minerType = EMinerType()
    speed = Int32Field()
    time = Int32Field()
    period = Int32Field()
    insertTarget = Int32Field()
    workstate = EWorkState()
    veins = ArrayField(Int32Field)
    currentVeinIndex = Int32Field()
    minimumVeinAmount = Int32Field()
    productId = Int32Field()
    productCount = Int32Field()
    seed = UInt32Field()
