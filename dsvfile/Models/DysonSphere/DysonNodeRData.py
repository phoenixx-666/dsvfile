from ...Fields import FloatField
from . import Model, Int32Field


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
