from Fields import Int32Field, FloatField
from Models import Model


"""
DysonNodeRData
{
    int32 version = 0
    int32 id
    int32 layerId
    float pos_x
    float pos_y
    float pos_z
    float angularVel
    float layerRot_x
    float layerRot_y
    float layerRot_z
    float layerRot_w
}
"""


class DysonNodeRData(Model):
    version = Int32Field()
    id = Int32Field()
    layerId = Int32Field()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    angularVel = FloatField()
    layerRot_x = FloatField()
    layerRot_y = FloatField()
    layerRot_z = FloatField()
    layerRot_w = FloatField()
