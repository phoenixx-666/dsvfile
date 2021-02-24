from ...Fields import FloatField
from . import Model, Int32Field, ArrayField


class PowerNetworkNode(Model):
    version = Int32Field()
    id = Int32Field()
    x = FloatField()
    y = FloatField()
    z = FloatField()
    connDistance2 = FloatField()
    coverRadius2 = FloatField()
    genId = Int32Field()
    accId = Int32Field()
    excId = Int32Field()
    numConnIdsForLoad = Int32Field()
    numLineIdsForLoad = Int32Field()
    numConsumers = Int32Field()
    connIdsForLoad = ArrayField(Int32Field, length_field='numConnIdsForLoad')
    lineIdsForLoad = ArrayField(Int32Field, length_field='numLineIdsForLoad')
    consumers = ArrayField(Int32Field, length_field='numConsumers')
