from ...Fields import FloatField
from . import Model, Int32Field, ArrayField


"""
PowerNetworkStructures::Node
{
    int32 version = 0
    int32 id
    float x
    float y
    float z
    float connDistance2
    float coverRadius2
    int32 genId
    int32 accId
    int32 excId
    int32 numConnIdsForLoad
    int32 numLineIdsForLoad
    int32 numConsumers
    int32 connIdsForLoad[numConnIdsForLoad]
    int32 lineIdsForLoad[numLineIdsForLoad]
    int32 consumers[numConsumers]
}
"""


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
