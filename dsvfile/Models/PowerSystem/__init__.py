from ...Fields import ModelField, ArrayField, ConditionalField
from ...Func import eq, decr
from .. import Model, Int32Field
from .PowerGeneratorComponent import PowerGeneratorComponent
from .PowerNodeComponent import PowerNodeComponent
from .PowerConsumerComponent import PowerConsumerComponent
from .PowerAccumulatorComponent import PowerAccumulatorComponent
from .PowerExchangerComponent import PowerExchangerComponent
from .PowerNetwork import PowerNetwork


"""
PowerSystem
{
    int32 version = 0
    int32 generatorCapacity
    int32 genCursor
    int32 genRecycleCursor
    PowerGeneratorComponent genPool[genCursor - 1]
    int32 genRecycle[genRecycleCursor]
    int32 nodeCapacity
    int32 nodeCursor
    int32 nodeRecycleCursor
    PowerNodeComponent nodePool[nodeCursor - 1]
    int32 nodeRecycle[nodeRecycleCursor]
    int32 consumerCapacity
    int32 consumerCursor
    int32 consumerRecycleCursor
    PowerConsumerComponent consumerPool[consumerCursor - 1]
    int32 consumerRecycle[consumerRecycleCursor]
    int32 accumulatorCapacity
    int32 accCursor
    int32 accRecycleCursor
    PowerAccumulatorComponent accPool[accCursor - 1]
    int32 accRecycle[accRecycleCursor]
    int32 exchangerCapacity
    int32 excCursor
    int32 excRecycleCursor
    PowerExchangerComponent excPool[excCursor - 1]
    int32 excRecycle[excRecycleCursor]
    int32 networkCapacity
    int32 netCursor
    int32 netRecycleCursor
    [netCursor] {
        int32 powerNetworkIncludedFlag
        PowerNetwork netPool (powerNetworkIncludedFlag == 1)
    }
    int32 netRecycle[netRecycleCursor]
}
"""


class PowerNetworkSwitch(Model):
    powerNetworkIncludedFlag = Int32Field()
    netPool = ConditionalField(lambda: ModelField(PowerNetwork),
                               arg_fields='powerNetworkIncludedFlag', condition_func=eq(1))


class PowerSystem(Model):
    version = Int32Field()
    generatorCapacity = Int32Field()
    genCursor = Int32Field()
    genRecycleCursor = Int32Field()
    genPool = ArrayField(lambda: ModelField(PowerGeneratorComponent), length_field='genCursor', length_func=decr())
    genRecycle = ArrayField(Int32Field, length_field='genRecycleCursor')
    nodeCapacity = Int32Field()
    nodeCursor = Int32Field()
    nodeRecycleCursor = Int32Field()
    nodePool = ArrayField(lambda: ModelField(PowerNodeComponent), length_field='nodeCursor', length_func=decr())
    nodeRecycle = ArrayField(Int32Field, length_field='nodeRecycleCursor')
    consumerCapacity = Int32Field()
    consumerCursor = Int32Field()
    consumerRecycleCursor = Int32Field()
    consumerPool = ArrayField(lambda: ModelField(PowerConsumerComponent),
                              length_field='consumerCursor', length_func=decr())
    consumerRecycle = ArrayField(Int32Field, length_field='consumerRecycleCursor')
    accumulatorCapacity = Int32Field()
    accCursor = Int32Field()
    accRecycleCursor = Int32Field()
    accPool = ArrayField(lambda: ModelField(PowerAccumulatorComponent),
                         length_field='accCursor', length_func=decr())
    accRecycle = ArrayField(Int32Field, length_field='accRecycleCursor')
    exchangerCapacity = Int32Field()
    excCursor = Int32Field()
    excRecycleCursor = Int32Field()
    excPool = ArrayField(lambda: ModelField(PowerExchangerComponent), length_field='excCursor', length_func=decr())
    excRecycle = ArrayField(Int32Field, length_field='excRecycleCursor')
    networkCapacity = Int32Field()
    netCursor = Int32Field()
    netRecycleCursor = Int32Field()
    netPool = ArrayField(lambda: ModelField(PowerNetworkSwitch), length_field='netCursor')
    netRecycle = ArrayField(Int32Field, length_field='netRecycleCursor')
