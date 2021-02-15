from Field import Int32Field, DoubleField, EnumField, BoolField
from Reader import Reader

"""
PlayerNavigation
{
    int32 version = 0
    uint8_bool navigating
    int32 naviAstroId
    double naviTarget_x
    double naviTarget_y
    double naviTarget_z
    uint8_bool useFly
    uint8_bool useSail
    uint8_bool useWarp
    int32 ENaviStage stage (None, Departure, OriginOrbit, AccOrbit, Space, DestOrbit, Approaching)
    double flyThreshold
    double sailThreshold
    double warpThreshold
    double maxSailSpeed
}
"""


class ENaviStage(EnumField):
    enum_values = ('None', 'Departure', 'OriginOrbit', 'AccOrbit', 'Space', 'DestOrbit', 'Approaching')


class PlayerNavigation(Reader):
    version = Int32Field()
    navigating = BoolField()
    naviAstroId = Int32Field()
    naviTarget_x = DoubleField()
    naviTarget_y = DoubleField()
    naviTarget_z = DoubleField()
    useFly = BoolField()
    useSail = BoolField()
    useWarp = BoolField()
    stage = ENaviStage()
    flyThreshold = DoubleField()
    sailThreshold = DoubleField()
    warpThreshold = DoubleField()
    maxSailSpeed = DoubleField()