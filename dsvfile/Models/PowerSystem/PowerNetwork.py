from . import Model, Int32Field, ModelField, ArrayField
from .PowerNetworkNode import PowerNetworkNode


class PowerNetwork(Model):
    version = Int32Field()
    id = Int32Field()
    numNodes = Int32Field()
    numConsumers = Int32Field()
    numGenerators = Int32Field()
    numAccumulators = Int32Field()
    numExchangers = Int32Field()
    nodes = ArrayField(ModelField(PowerNetworkNode), length_field='numNodes')
    consumers = ArrayField(Int32Field, length_field='numConsumers')
    generators = ArrayField(Int32Field, length_field='numGenerators')
    accumulators = ArrayField(Int32Field, length_field='numAccumulators')
    exchangers = ArrayField(Int32Field, length_field='numExchangers')
