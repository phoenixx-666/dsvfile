from ..Fields import FloatField, ArrayField, ConditionalField
from ..Func import ge
from . import Model, Int32Field


class GameDesc(Model):
    version = Int32Field()
    galaxyAlgo = Int32Field()
    galaxySeed = Int32Field()
    starCount = Int32Field()
    playerProto = Int32Field()
    resourceMultiplier = ConditionalField(FloatField, arg_fields='version', condition_func=ge(2))
    themeIds = ConditionalField(ArrayField(Int32Field), arg_fields='version', condition_func=ge(1))
