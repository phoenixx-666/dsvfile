from ...Fields import UInt32Field
from ...Fields.Enums import EMinerType, EWorkState
from . import Model, Int32Field, ArrayField


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
