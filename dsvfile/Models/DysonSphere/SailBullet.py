from ...Fields import FloatField, DoubleField
from . import Model, Int32Field


"""
SailBullet
{
    int32 version = 0
    int32 id
    float t
    float maxt
    int32 state
    float rBegin_x
    float rBegin_y
    float rBegin_z
    float rEnd_x
    float rEnd_y
    float rEnd_z
    float lBegin_x
    float lBegin_y
    float lBegin_z
    float uEndVel_x
    float uEndVel_y
    float uEndVel_z
    double uBegin_x
    double uBegin_y
    double uBegin_z
    double uEnd_x
    double uEnd_y
    double uEnd_z
}
"""


class SailBullet(Model):
    version = Int32Field()
    id = Int32Field()
    t = FloatField()
    maxt = FloatField()
    state = Int32Field()
    rBegin_x = FloatField()
    rBegin_y = FloatField()
    rBegin_z = FloatField()
    rEnd_x = FloatField()
    rEnd_y = FloatField()
    rEnd_z = FloatField()
    lBegin_x = FloatField()
    lBegin_y = FloatField()
    lBegin_z = FloatField()
    uEndVel_x = FloatField()
    uEndVel_y = FloatField()
    uEndVel_z = FloatField()
    uBegin_x = DoubleField()
    uBegin_y = DoubleField()
    uBegin_z = DoubleField()
    uEnd_x = DoubleField()
    uEnd_y = DoubleField()
    uEnd_z = DoubleField()
