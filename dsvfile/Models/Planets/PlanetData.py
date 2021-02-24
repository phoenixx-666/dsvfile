from ...Fields import Int64Field, ByteStringField
from ...Fields.Enums import EVeinType
from . import Model, Int32Field, FloatField, ArrayField, ModelField


class VeinGroup(Model):
    veinType = EVeinType()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    count = Int32Field()
    amount = Int64Field()


class PlanetData(Model):
    modData = ByteStringField()
    veinAmounts = ArrayField(Int64Field)
    veinGroups = ArrayField(lambda: ModelField(VeinGroup))
