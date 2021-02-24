from ...Fields import UInt32Field, FloatField, BoolField
from . import Model, Int32Field


class FractionateComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    belt0 = Int32Field()
    belt1 = Int32Field()
    belt2 = Int32Field()
    isOutput0 = BoolField()
    isOutput1 = BoolField()
    isOutput2 = BoolField()
    isWorking = BoolField()
    produceProb = FloatField()
    need = Int32Field()
    product = Int32Field()
    needCurrCount = Int32Field()
    productCurrCount = Int32Field()
    oriProductCurrCount = Int32Field()
    progress = Int32Field()
    isRand = BoolField()
    fractionateSuccess = BoolField()
    needMaxCount = Int32Field()
    productMaxCount = Int32Field()
    oriProductMaxCount = Int32Field()
    seed = UInt32Field()
