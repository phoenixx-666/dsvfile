from ...Fields import BoolField
from . import Model, Int32Field


class TankComponent(Model):
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
