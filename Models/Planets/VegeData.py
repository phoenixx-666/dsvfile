from Fields import UInt8Field, Int16Field, Int32Field, FloatField
from Models import Model


"""
VegeData
{
    uint8 version = 0
    int32 id
    int16 protoId
    int16 modelIndex
    int16 hp
    float pos_x
    float pos_y
    float pos_z
    float rot_x
    float rot_y
    float rot_z
    float rot_w
    float scl_x
    float scl_y
    float scl_z
}
"""


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
