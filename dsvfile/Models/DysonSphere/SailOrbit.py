from ...Fields import FloatField, BoolField
from . import Model, Int32Field


class SailOrbit(Model):
    version = Int32Field()
    id = Int32Field()
    radius = FloatField()
    rotation_x = FloatField()
    rotation_y = FloatField()
    rotation_z = FloatField()
    rotation_w = FloatField()
    up_x = FloatField()
    up_y = FloatField()
    up_z = FloatField()
    count = Int32Field()
    enabled = BoolField()
