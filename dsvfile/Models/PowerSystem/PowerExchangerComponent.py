from ...Fields import Int16Field, Int64Field, FloatField, BoolField, ConditionalBlockStart
from ...Func import ge
from . import Model, Int32Field


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
