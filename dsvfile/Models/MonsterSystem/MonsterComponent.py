from ...Fields import FloatField
from ...Fields.Enums import EMonsterState
from . import Model, Int32Field


class MonsterComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    walkSpeed = FloatField()
    point0_x = FloatField()
    point0_y = FloatField()
    point0_z = FloatField()
    point1_x = FloatField()
    point1_y = FloatField()
    point1_z = FloatField()
    point2_x = FloatField()
    point2_y = FloatField()
    point2_z = FloatField()
    direction = Int32Field()
    stopTime = FloatField()
    t = FloatField()
    stopCurrentTime = FloatField()
    monsterState = EMonsterState()
    stepDistance = FloatField()
