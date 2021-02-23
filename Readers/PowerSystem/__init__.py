from Field import Int32Field, ReaderField, ArrayField, ConditionalField
from Func import eq, decr
from Reader import Reader
from Readers.PowerSystem.PowerGeneratorComponent import PowerGeneratorComponent
from Readers.PowerSystem.PowerNodeComponent import PowerNodeComponent
from Readers.PowerSystem.PowerConsumerComponent import PowerConsumerComponent
from Readers.PowerSystem.PowerAccumulatorComponent import PowerAccumulatorComponent
from Readers.PowerSystem.PowerExchangerComponent import PowerExchangerComponent
from Readers.PowerSystem.PowerNetwork import PowerNetwork


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


class PowerNetworkSwitch(Reader):
    powerNetworkIncludedFlag = Int32Field()
    netPool = ConditionalField(lambda: ReaderField(PowerNetwork),
                               arg_fields='powerNetworkIncludedFlag', condition_func=eq(1))


class PowerSystem(Reader):
    version = Int32Field()
    generatorCapacity = Int32Field()
    genCursor = Int32Field()
    genRecycleCursor = Int32Field()
    genPool = ArrayField(lambda: ReaderField(PowerGeneratorComponent), length_field='genCursor', length_function=decr())
    genRecycle = ArrayField(Int32Field, length_field='genRecycleCursor')
    nodeCapacity = Int32Field()
    nodeCursor = Int32Field()
    nodeRecycleCursor = Int32Field()
    nodePool = ArrayField(lambda: ReaderField(PowerNodeComponent), length_field='nodeCursor', length_function=decr())
    nodeRecycle = ArrayField(Int32Field, length_field='nodeRecycleCursor')
    consumerCapacity = Int32Field()
    consumerCursor = Int32Field()
    consumerRecycleCursor = Int32Field()
    consumerPool = ArrayField(lambda: ReaderField(PowerConsumerComponent),
                              length_field='consumerCursor', length_function=decr())
    consumerRecycle = ArrayField(Int32Field, length_field='consumerRecycleCursor')
    accumulatorCapacity = Int32Field()
    accCursor = Int32Field()
    accRecycleCursor = Int32Field()
    accPool = ArrayField(lambda: ReaderField(PowerAccumulatorComponent),
                         length_field='accCursor', length_function=decr())
    accRecycle = ArrayField(Int32Field, length_field='accRecycleCursor')
    exchangerCapacity = Int32Field()
    excCursor = Int32Field()
    excRecycleCursor = Int32Field()
    excPool = ArrayField(lambda: ReaderField(PowerExchangerComponent), length_field='excCursor', length_function=decr())
    excRecycle = ArrayField(Int32Field, length_field='excRecycleCursor')
    networkCapacity = Int32Field()
    netCursor = Int32Field()
    netRecycleCursor = Int32Field()
    netPool = ArrayField(lambda: ReaderField(PowerNetworkSwitch), length_field='netCursor')
    netRecycle = ArrayField(Int32Field, length_field='netRecycleCursor')
