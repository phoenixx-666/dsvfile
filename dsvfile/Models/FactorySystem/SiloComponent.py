from ...Fields import FloatField, BoolField
from . import Model, Int32Field


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
