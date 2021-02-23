from ..Fields import FloatField, ModelField, ArrayField
from . import Model, Int32Field


"""
CargoContainer
{
    int32 version = 0
    int32 poolCapacity
    int32 cursor
    int32 recycleBegin
    int32 recycleEnd
    cargoPool[cursor] {
        int32 item
        float position_x
        float position_y
        float position_z
        float rotation_x
        float rotation_y
        float rotation_z
        float rotation_w
    }
    int32 recycleIds[poolCapacity]
}
"""


class Cargo(Model):
    item = Int32Field()
    position_x = FloatField()
    position_y = FloatField()
    position_z = FloatField()
    rotation_x = FloatField()
    rotation_y = FloatField()
    rotation_z = FloatField()
    rotation_w = FloatField()


class CargoContainer(Model):
    version = Int32Field()
    poolCapacity = Int32Field()
    cursor = Int32Field()
    recycleBegin = Int32Field()
    recycleEnd = Int32Field()
    cargoPool = ArrayField(lambda: ModelField(Cargo), length_field='cursor')
    recycleIds = ArrayField(Int32Field, length_field='poolCapacity')
