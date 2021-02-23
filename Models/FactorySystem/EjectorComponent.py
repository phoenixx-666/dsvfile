from Fields import Int32Field, FloatField, BoolField
from Models import Model


"""
EjectorComponent
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
    int32 orbitId
    float pivotY
    float muzzleY
    float localPosN_x
    float localPosN_y
    float localPosN_z
    float localAlt
    float localRot_x
    float localRot_y
    float localRot_z
    float localRot_w
    float localDir_x
    float localDir_y
    float localDir_z
}
"""


class EjectorComponent(Model):
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
    orbitId = Int32Field()
    pivotY = FloatField()
    muzzleY = FloatField()
    localPosN_x = FloatField()
    localPosN_y = FloatField()
    localPosN_z = FloatField()
    localAlt = FloatField()
    localRot_x = FloatField()
    localRot_y = FloatField()
    localRot_z = FloatField()
    localRot_w = FloatField()
    localDir_x = FloatField()
    localDir_y = FloatField()
    localDir_z = FloatField()
