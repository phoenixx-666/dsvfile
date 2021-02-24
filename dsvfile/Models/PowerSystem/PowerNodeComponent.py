from ...Fields import FloatField, BoolField
from . import Model, Int32Field


class PowerNodeComponent(Model):
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
