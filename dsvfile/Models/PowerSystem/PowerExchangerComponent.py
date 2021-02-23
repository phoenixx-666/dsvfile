from ...Fields import Int16Field, Int64Field, FloatField, BoolField, ConditionalBlockStart
from ...Func import ge
from . import Model, Int32Field


"""
PowerExchangerComponent
{
    int32 version = 1
    int32 id
    int32 entityId
    int32 networkId
    int16 emptyCount
    int16 fullCount
    float targetState
    float state
    int64 energyPerTick
    int64 curPoolEnergy
    int64 poolMaxEnergy
    int32 emptyId
    int32 fullId
    int32 belt0 (version >= 1)
    int32 belt1 (version >= 1)
    int32 belt2 (version >= 1)
    int32 belt3 (version >= 1)
    uint8_bool isOutput0 (version >= 1)
    uint8_bool isOutput1 (version >= 1)
    uint8_bool isOutput2 (version >= 1)
    uint8_bool isOutput3 (version >= 1)
    int32 outputSlot (version >= 1)
    int32 inputSlot (version >= 1)
    int32 outputRectify (version >= 1)
    int32 inputRectify (version >= 1)
}
"""


class PowerExchangerComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    emptyCount = Int16Field()
    fullCount = Int16Field()
    targetState = FloatField()
    state = FloatField()
    energyPerTick = Int64Field()
    curPoolEnergy = Int64Field()
    poolMaxEnergy = Int64Field()
    emptyId = Int32Field()
    fullId = Int32Field()
    versionCheck = ConditionalBlockStart('version', ge(1))
    belt0 = Int32Field()
    belt1 = Int32Field()
    belt2 = Int32Field()
    belt3 = Int32Field()
    isOutput0 = BoolField()
    isOutput1 = BoolField()
    isOutput2 = BoolField()
    isOutput3 = BoolField()
    outputSlot = Int32Field()
    inputSlot = Int32Field()
    outputRectify = Int32Field()
    inputRectify = Int32Field()
