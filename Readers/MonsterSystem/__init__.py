from Field import Int32Field, FloatField, ReaderField, ArrayField
from Func import decr
from Reader import Reader
from Readers.MonsterSystem.MonsterComponent import MonsterComponent


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


class MonsterSystem(Reader):
    version = Int32Field()
    monsterCapacity = Int32Field()
    monsterCursor = Int32Field()
    monsterRecycleCursor = Int32Field()
    monsterPool = ArrayField(lambda: ReaderField(MonsterComponent),
                             length_field='monsterCursor', length_function=decr())
    monsterRecycle = ArrayField(Int32Field, length_field='monsterRecycleCursor')
