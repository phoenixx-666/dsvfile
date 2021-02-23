from Fields import Int32Field, Int64Field, ModelField, ArrayField, ConditionalField
from Func import decr, ge
from Models import Model


"""
FactoryProductionStat
{
    int32 version = 1
    int32 productCapacity
    int32 productCursor
    ProductStat productPool[productCursor - 1]
    int32 numPowerPool, max 5
    PowerStat powerPool[numPowerPool]
    int32 numProductIndices
    int32 productIndices[numProductIndices]
    int64 energyConsumption (version >= 1)
}

ProductStat
{
    int32 version = 0
    int32 numCount:  Saved as 7200.  Reads more or less, but only stores up to 7200, and enforces abs.
    int32 count[numCount]
    int32 numCursor:  Saved as 12.  Reads more or less, but only stores up to 12.
    int32 cursor[numCount]
    int32 numTotal:  Saved as 14.  Reads more or less, but only stores up to 14, and enforces abs.
    int32 total[numCount]
    int32 itemId
}

PowerStat
{
    int32 version = 0
    int32 numEnergy:  Saved as 3600.  Reads more or less, but only stores up to 3600, and enforces abs.
    int64 energy[numCount]
    int32 numCursor:  Saved as 6.  Reads more or less, but only stores up to 6.
    int32 cursor[numCount]
    int32 numTotal:  Saved as 7.  Reads more or less, but only stores up to 7, and enforces abs.
    int64 total[numCount]
}
"""


class ProductStat(Model):
    version = Int32Field()
    count = ArrayField(Int32Field)
    cursor = ArrayField(Int32Field)
    total = ArrayField(Int32Field)
    itemId = Int32Field()


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
