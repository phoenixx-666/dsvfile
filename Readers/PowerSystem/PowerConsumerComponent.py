from Field import Int32Field, Int64Field, FloatField
from Reader import Reader


"""
PowerConsumerComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 networkId
    float plugPos_x
    float plugPos_y
    float plugPos_z
    int64 requiredEnergy
    int64 servedEnergy
    int64 workEnergyPerTick
    int64 idleEnergyPerTick
}
"""


class PowerConsumerComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    plugPos_x = FloatField()
    plugPos_y = FloatField()
    plugPos_z = FloatField()
    requiredEnergy = Int64Field()
    servedEnergy = Int64Field()
    workEnergyPerTick = Int64Field()
    idleEnergyPerTick = Int64Field()
