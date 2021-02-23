from Fields import Int32Field, FloatField, DoubleField
from Models import Model

"""
ShipData 
{
    int32 version = 0
    int32 stage
    int32 planetA
    int32 planetB
    double uPos_x
    double uPos_y
    double uPos_z
    float uVel_x
    float uVel_y
    float uVel_z
    float uSpeed
    float warpState
    float uRot_x
    float uRot_y
    float uRot_z
    float uRot_w
    float uAngularVel_x
    float uAngularVel_y
    float uAngularVel_z
    float uAngularSpeed
    double pPosTemp_x
    double pPosTemp_y
    double pPosTemp_z
    float pRotTemp_x
    float pRotTemp_y
    float pRotTemp_z
    float pRotTemp_w
    int32 otherGId
    int32 direction
    float t
    int32 itemId
    int32 itemCount
    int32 gene
    int32 shipIndex
    int32 warperCnt
}
"""


class ShipData(Model):
    version = Int32Field()
    stage = Int32Field()
    planetA = Int32Field()
    planetB = Int32Field()
    uPos_x = DoubleField()
    uPos_y = DoubleField()
    uPos_z = DoubleField()
    uVel_x = FloatField()
    uVel_y = FloatField()
    uVel_z = FloatField()
    uSpeed = FloatField()
    warpState = FloatField()
    uRot_x = FloatField()
    uRot_y = FloatField()
    uRot_z = FloatField()
    uRot_w = FloatField()
    uAngularVel_x = FloatField()
    uAngularVel_y = FloatField()
    uAngularVel_z = FloatField()
    uAngularSpeed = FloatField()
    pPosTemp_x = DoubleField()
    pPosTemp_y = DoubleField()
    pPosTemp_z = DoubleField()
    pRotTemp_x = FloatField()
    pRotTemp_y = FloatField()
    pRotTemp_z = FloatField()
    pRotTemp_w = FloatField()
    otherGId = Int32Field()
    direction = Int32Field()
    t = FloatField()
    itemId = Int32Field()
    itemCount = Int32Field()
    gene = Int32Field()
    shipIndex = Int32Field()
    warperCnt = Int32Field()
