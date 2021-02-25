from ..Fields import FloatField, ModelField, ArrayField
from ..Fields.Enums import EItem
from . import Model, Int32Field


class Cargo(Model):
    item = EItem()
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
    cargoPool = ArrayField(ModelField(Cargo), length_field='cursor')
    recycleIds = ArrayField(Int32Field, length_field='poolCapacity')
