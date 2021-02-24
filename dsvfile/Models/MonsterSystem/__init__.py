from ...Fields import ModelField, ArrayField
from ...Func import decr
from .. import Model, Int32Field
from .MonsterComponent import MonsterComponent


class MonsterSystem(Model):
    version = Int32Field()
    monsterCapacity = Int32Field()
    monsterCursor = Int32Field()
    monsterRecycleCursor = Int32Field()
    monsterPool = ArrayField(lambda: ModelField(MonsterComponent),
                             length_field='monsterCursor', length_func=decr())
    monsterRecycle = ArrayField(Int32Field, length_field='monsterRecycleCursor')
