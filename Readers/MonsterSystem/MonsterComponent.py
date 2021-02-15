from Field import Int32Field, FloatField
from Field.Enums import EMonsterState
from Reader import Reader


"""
MonsterComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    float walkSpeed
    float point0_x
    float point0_y
    float point0_z
    float point1_x
    float point1_y
    float point1_z
    float point2_x
    float point2_y
    float point2_z
    int32 direction
    float stopTime
    float t
    float stopCurrentTime
    int32 EMonsterState monsterState (Null, Stopped, Wandering)
    float stepDistance
}
"""


class MonsterComponent(Reader):
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
