from Field import Int16Field, Int32Field, Int64Field, FloatField, BoolField
from Reader import Reader


"""
PowerGeneratorComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 networkId
    uint8_bool photovoltaic
    uint8_bool wind
    uint8_bool gamma
    int64 genEnergyPerTick
    int64 useFuelPerTick
    int16 fuelMask
    int64 fuelEnergy
    int16 curFuelId
    int16 fuelId
    int16 fuelCount
    int64 fuelHeat
    int32 catalystId
    int32 catalystPoint
    int32 productId
    float productCount
    int64 productHeat
    float warmup
    float ionEnhance
    float x
    float y
    float z
}
"""


class PowerGeneratorComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    photovoltaic = BoolField()
    wind = BoolField()
    gamma = BoolField()
    genEnergyPerTick = Int64Field()
    useFuelPerTick = Int64Field()
    fuelMask = Int16Field()
    fuelEnergy = Int64Field()
    curFuelId = Int16Field()
    fuelId = Int16Field()
    fuelCount = Int16Field()
    fuelHeat = Int64Field()
    catalystId = Int32Field()
    catalystPoint = Int32Field()
    productId = Int32Field()
    productCount = FloatField()
    productHeat = Int64Field()
    warmup = FloatField()
    ionEnhance = FloatField()
    x = FloatField()
    y = FloatField()
    z = FloatField()
