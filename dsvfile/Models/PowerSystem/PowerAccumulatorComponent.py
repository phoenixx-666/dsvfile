from ...Fields import Int64Field
from . import Model, Int32Field


class PowerAccumulatorComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    inputEnergyPerTick = Int64Field()
    outputEnergyPerTick = Int64Field()
    curEnergy = Int64Field()
    maxEnergy = Int64Field()
