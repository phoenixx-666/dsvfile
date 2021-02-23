from Fields import Int32Field, FloatField, ArrayField, ConditionalField
from Func import ge
from Models import Model


"""
GameDesc
{
    int32 version = 2
    int32 galaxyAlgo
    int32 galaxySeed
    int32 starCount
    int32 playerProto
    float resourceMultiplier (version >= 2)
    int32 numThemeIds (version >= 1)
    int32 themeIds[numThemeIds] (version >= 1)
}
"""


class GameDesc(Model):
    version = Int32Field()
    galaxyAlgo = Int32Field()
    galaxySeed = Int32Field()
    starCount = Int32Field()
    playerProto = Int32Field()
    resourceMultiplier = ConditionalField(FloatField, arg_fields='version', condition_func=ge(2))
    themeIds = ConditionalField(lambda: ArrayField(Int32Field), arg_fields='version', condition_func=ge(1))
