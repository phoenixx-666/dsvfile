from ...Fields import FloatField, DoubleField
from . import Model, Int32Field


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
