from ...Fields import FloatField, DoubleField
from . import Model, Int32Field


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
