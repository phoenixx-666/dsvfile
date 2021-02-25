from ..Fields import Int64Field, FloatField, BoolField, ModelField, ArrayField, ConditionalField
from ..Fields.Enums import ERecipe
from ..Func import ge
from . import Model, Int32Field


class TechState(Model):
    techProtoIndex = Int32Field()
    techState_unlocked = BoolField()
    techState_curLevel = Int32Field()
    techState_maxLevel = Int32Field()
    techState_hashUploaded = Int64Field()
    techState_hashNeeded = Int64Field()


class GameHistoryData(Model):
    version = Int32Field()
    recipeUnlocked = ArrayField(ERecipe)
    tutorialUnlocked = ConditionalField(ArrayField(Int32Field), arg_fields='version', condition_func=ge(2))
    featureKeys = ArrayField(Int32Field)
    techStates = ArrayField(ModelField(TechState))
    autoManageLabItems = BoolField()
    currentTech = Int32Field()
    techQueue = ConditionalField(ArrayField(Int32Field), arg_fields='version', condition_func=ge(1))
    universeObserveLevel = Int32Field()
    solarSailLife = FloatField()
    solarEnergyLossRate = FloatField()
    useIonLayer = BoolField()
    inserterStackCount = Int32Field()
    logisticDroneSpeed = FloatField()
    logisticDroneSpeedScale = FloatField()
    logisticDroneCarries = Int32Field()
    logisticShipSailSpeed = FloatField()
    logisticShipWarpSpeed = FloatField()
    logisticShipSpeedScale = FloatField()
    logisticShipWarpDrive = BoolField()
    logisticShipCarries = Int32Field()
    miningCostRate = FloatField()
    miningSpeedScale = FloatField()
    storageLevel = Int32Field()
    labLevel = Int32Field()
    techSpeed = Int32Field()
    dysonNodeLatitude = FloatField()
    universeMatrixPointUploaded = Int64Field()
    missionAccomplished = BoolField()
