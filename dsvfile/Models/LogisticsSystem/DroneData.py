from ...Fields import FloatField
from . import Model, Int32Field


"""
DroneData
{
    int32 version = 0
    float begin_x
    float begin_y
    float begin_z
    float end_x
    float end_y
    float end_z
    int32 endId
    float direction
    float maxt
    float t
    int32 itemId
    int32 itemCount
    int32 gene
}
"""


class DroneData(Model):
    version = Int32Field()
    begin_x = FloatField()
    begin_y = FloatField()
    begin_z = FloatField()
    end_x = FloatField()
    end_y = FloatField()
    end_z = FloatField()
    endId = Int32Field()
    direction = FloatField()
    maxt = FloatField()
    t = FloatField()
    itemId = Int32Field()
    itemCount = Int32Field()
    gene = Int32Field()
