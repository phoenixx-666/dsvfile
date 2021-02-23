from Fields import Int32Field, FloatField, BoolField
from Models import Model


"""
SiloComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 planetId
    int32 pcId
    int32 direction
    int32 time
    uint8_bool fired
    int32 chargeSpend
    int32 coldSpend
    int32 bulletId
    int32 bulletCount
    int32 autoIndex
    uint8_bool hasNode
    float localPos_x
    float localPos_y
    float localPos_z
    float localRot_x
    float localRot_y
    float localRot_z
    float localRot_w
}
"""


class SiloComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    planetId = Int32Field()
    pcId = Int32Field()
    direction = Int32Field()
    time = Int32Field()
    fired = BoolField()
    chargeSpend = Int32Field()
    coldSpend = Int32Field()
    bulletId = Int32Field()
    bulletCount = Int32Field()
    autoIndex = Int32Field()
    hasNode = BoolField()
    localPos_x = FloatField()
    localPos_y = FloatField()
    localPos_z = FloatField()
    localRot_x = FloatField()
    localRot_y = FloatField()
    localRot_z = FloatField()
    localRot_w = FloatField()
