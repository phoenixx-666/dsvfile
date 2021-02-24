from ...Fields import UInt8Field, Int16Field
from . import Model, Int32Field, FloatField


class VegeData(Model):
    version = UInt8Field()
    id = Int32Field()
    protoId = Int16Field()
    modelIndex = Int16Field()
    hp = Int16Field()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    rot_x = FloatField()
    rot_y = FloatField()
    rot_z = FloatField()
    rot_w = FloatField()
    scl_x = FloatField()
    scl_y = FloatField()
    scl_z = FloatField()
