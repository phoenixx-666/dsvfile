from Field import Int32Field, Int64Field, FloatField, BoolField, ReaderField, ArrayField
from Reader import Reader

"""
GameHistoryData
{
    int32 version = 2
    int32 numRecipeUnlocked
    int32 recipeUnlocked[numRecipeUnlocked]
    int32 numTutorialUnlocked (version >= 2)
    int32 tutorialUnlocked[numTutorialUnlocked] (version >= 2)
    int32 numFeatureKeys
    int32 featureKeys[numFeatureKeys]
    int32 numTechState
    TechState[numTechState] {
        int32 techProtoIndex  
        uint8_bool TechState_unlocked
        int32 TechState_curLevel
        int32 TechState_maxLevel
        int64 TechState_hashUploaded
        int64 TechState_hashNeeded
    }
    uint8_bool autoManageLabItems
    int32 currentTech
    int32 numTechQueue (version >= 1)
    int32 techQueue[numTechQueue] (version >= 1)
    int32 universeObserveLevel
    float solarSailLife
    float solarEnergyLossRate
    uint8_bool useIonLayer
    int32 inserterStackCount
    float logisticDroneSpeed
    float logisticDroneSpeedScale
    int32 logisticDroneCarries
    float logisticShipSailSpeed
    float logisticShipWarpSpeed
    float logisticShipSpeedScale
    uint8_bool logisticShipWarpDrive
    int32 logisticShipCarries
    float miningCostRate
    float miningSpeedScale
    int32 storageLevel
    int32 labLevel
    int32 techSpeed
    float dysonNodeLatitude
    int64 universeMatrixPointUploaded
    uint8_bool missionAccomplished
}
"""


class TechState(Reader):
    techProtoIndex = Int32Field()
    techState_unlocked = BoolField()
    techState_curLevel = Int32Field()
    techState_maxLevel = Int32Field()
    techState_hashUploaded = Int64Field()
    techState_hashNeeded = Int64Field()


class GameHistoryData(Reader):
    version = Int32Field()
    recipeUnlocked = ArrayField(Int32Field)
    tutorialUnlocked = ArrayField(Int32Field)
    featureKeys = ArrayField(Int32Field)
    techStates = ArrayField(lambda: ReaderField(TechState))
    autoManageLabItems = BoolField()
    currentTech = Int32Field()
    techQueue = ArrayField(Int32Field)
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
