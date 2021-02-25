from ..Fields import Int64Field, ModelField, ArrayField, ConditionalField
from ..Fields.Enums import EItem
from ..Func import decr, ge
from . import Model, Int32Field


class ProductStat(Model):
    version = Int32Field()
    count = ArrayField(Int32Field)
    cursor = ArrayField(Int32Field)
    total = ArrayField(Int32Field)
    itemId = EItem()


class PowerStat(Model):
    version = Int32Field()
    energy = ArrayField(Int64Field)
    cursor = ArrayField(Int32Field)
    total = ArrayField(Int64Field)


class FactoryProductionStat(Model):
    version = Int32Field()
    productCapacity = Int32Field()
    productCursor = Int32Field()
    productStat = ArrayField(lambda: ModelField(ProductStat),
                             length_field='productCursor', length_func=decr())
    powerStat = ArrayField(lambda: ModelField(PowerStat))
    productIndices = ArrayField(Int32Field)
    energyConsumption = ConditionalField(Int64Field, arg_fields='version', condition_func=ge(1))
