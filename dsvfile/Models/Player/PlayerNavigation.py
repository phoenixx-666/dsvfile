from ...Fields.Enums import ENaviStage
from . import Model, Int32Field, DoubleField, BoolField


class PlayerNavigation(Model):
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
