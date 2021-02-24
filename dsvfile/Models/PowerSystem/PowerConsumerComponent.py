from ...Fields import Int64Field, FloatField
from . import Model, Int32Field


class PowerConsumerComponent(Model):
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
