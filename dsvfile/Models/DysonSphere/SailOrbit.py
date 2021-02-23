from ...Fields import FloatField, BoolField
from . import Model, Int32Field


"""
SailOrbit
{
    int32 version = 0
    int32 id
    float radius
    float rotation_x
    float rotation_y
    float rotation_z
    float rotation_w
    float up_x
    float up_y
    float up_z
    int32 count
    uint8_bool enabled
}
"""


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
