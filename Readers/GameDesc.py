from Field import Int32Field, FloatField, ArrayField
from Reader import Reader


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


class GameDesc(Reader):
    version = Int32Field()
    galaxyAlgo = Int32Field()
    galaxySeed = Int32Field()
    starCount = Int32Field()
    playerProto = Int32Field()
    resourceMultiplier = FloatField()
    themeIds = ArrayField(Int32Field)
