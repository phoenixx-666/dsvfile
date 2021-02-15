from Field import Int32Field, FloatField, BoolField
from Reader import Reader


"""
PowerNodeComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 networkId
    uint8_bool isCharger
    int32 workEnergyPerTick
    int32 idleEnergyPerTick
    int32 requiredEnergy
    float powerPoint_x
    float powerPoint_y
    float powerPoint_z
    float connectDistance
    float coverRadius
}
"""


class PowerNodeComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    isCharger = BoolField()
    workEnergyPerTick = Int32Field()
    idleEnergyPerTick = Int32Field()
    requiredEnergy = Int32Field()
    powerPoint_x = FloatField()
    powerPoint_y = FloatField()
    powerPoint_z = FloatField()
    connectDistance = FloatField()
    coverRadius = FloatField()
