from ...Fields import FloatField, DoubleField
from . import Model, Int32Field


"""
DysonRocket
{
    int32 version = 0
    int32 id
    int32 nodeLayerId
    int32 nodeId
    int32 planetId
    float t
    float uSpeed
    double uPos_x
    double uPos_y
    double uPos_z
    float uRot_x
    float uRot_y
    float uRot_z
    float uRot_w
    float uVel_x
    float uVel_y
    float uVel_z
    float launch_x
    float launch_y
    float launch_z
}
"""


class DysonRocket(Model):
    version = Int32Field()
    id = Int32Field()
    nodeLayerId = Int32Field()
    nodeId = Int32Field()
    planetId = Int32Field()
    t = FloatField()
    uSpeed = FloatField()
    uPos_x = DoubleField()
    uPos_y = DoubleField()
    uPos_z = DoubleField()
    uRot_x = FloatField()
    uRot_y = FloatField()
    uRot_z = FloatField()
    uRot_w = FloatField()
    uVel_x = FloatField()
    uVel_y = FloatField()
    uVel_z = FloatField()
    launch_x = FloatField()
    launch_y = FloatField()
    launch_z = FloatField()
