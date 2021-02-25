from ...Fields import ModelField, ArrayField, ConditionalField
from ...Func import eq, decr
from .. import Model, Int32Field
from .PowerGeneratorComponent import PowerGeneratorComponent
from .PowerNodeComponent import PowerNodeComponent
from .PowerConsumerComponent import PowerConsumerComponent
from .PowerAccumulatorComponent import PowerAccumulatorComponent
from .PowerExchangerComponent import PowerExchangerComponent
from .PowerNetwork import PowerNetwork


class PowerNetworkSwitch(Model):
    powerNetworkIncludedFlag = Int32Field()
    netPool = ConditionalField(ModelField(PowerNetwork),
                               arg_fields='powerNetworkIncludedFlag', condition_func=eq(1))


class PowerSystem(Model):
    version = Int32Field()
    generatorCapacity = Int32Field()
    genCursor = Int32Field()
    genRecycleCursor = Int32Field()
    genPool = ArrayField(ModelField(PowerGeneratorComponent), length_field='genCursor', length_func=decr())
    genRecycle = ArrayField(Int32Field, length_field='genRecycleCursor')
    nodeCapacity = Int32Field()
    nodeCursor = Int32Field()
    nodeRecycleCursor = Int32Field()
    nodePool = ArrayField(ModelField(PowerNodeComponent), length_field='nodeCursor', length_func=decr())
    nodeRecycle = ArrayField(Int32Field, length_field='nodeRecycleCursor')
    consumerCapacity = Int32Field()
    consumerCursor = Int32Field()
    consumerRecycleCursor = Int32Field()
    consumerPool = ArrayField(ModelField(PowerConsumerComponent),
                              length_field='consumerCursor', length_func=decr())
    consumerRecycle = ArrayField(Int32Field, length_field='consumerRecycleCursor')
    accumulatorCapacity = Int32Field()
    accCursor = Int32Field()
    accRecycleCursor = Int32Field()
    accPool = ArrayField(ModelField(PowerAccumulatorComponent),
                         length_field='accCursor', length_func=decr())
    accRecycle = ArrayField(Int32Field, length_field='accRecycleCursor')
    exchangerCapacity = Int32Field()
    excCursor = Int32Field()
    excRecycleCursor = Int32Field()
    excPool = ArrayField(ModelField(PowerExchangerComponent), length_field='excCursor', length_func=decr())
    excRecycle = ArrayField(Int32Field, length_field='excRecycleCursor')
    networkCapacity = Int32Field()
    netCursor = Int32Field()
    netRecycleCursor = Int32Field()
    netPool = ArrayField(ModelField(PowerNetworkSwitch), length_field='netCursor')
    netRecycle = ArrayField(Int32Field, length_field='netRecycleCursor')
