from Field import Int32Field, Int64Field
from Reader import Reader


"""
PowerAccumulatorComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 networkId
    int64 inputEnergyPerTick
    int64 outputEnergyPerTick
    int64 curEnergy
    int64 maxEnergy
}
"""


class PowerAccumulatorComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    networkId = Int32Field()
    inputEnergyPerTick = Int64Field()
    outputEnergyPerTick = Int64Field()
    curEnergy = Int64Field()
    maxEnergy = Int64Field()
