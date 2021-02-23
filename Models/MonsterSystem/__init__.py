from Fields import Int32Field, ModelField, ArrayField
from Func import decr
from Models import Model
from Models.MonsterSystem.MonsterComponent import MonsterComponent


"""
MonsterSystem
{
    int32 version = 0
    int32 monsterCapacity
    int32 monsterCursor
    int32 monsterRecycleCursor
    MonsterComponent monsterPool[monsterCursor - 1]
    int32 monsterRecycle[monsterRecycleCursor]
}
"""


class MonsterSystem(Model):
    version = Int32Field()
    monsterCapacity = Int32Field()
    monsterCursor = Int32Field()
    monsterRecycleCursor = Int32Field()
    monsterPool = ArrayField(lambda: ModelField(MonsterComponent),
                             length_field='monsterCursor', length_func=decr())
    monsterRecycle = ArrayField(Int32Field, length_field='monsterRecycleCursor')
