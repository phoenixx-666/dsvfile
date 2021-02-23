from ...Fields import Int64Field, UInt64Field, FloatField, DoubleField, StringField, BoolField, ConditionalBlockStart
from ...Func import g, ge
from . import Model, Int32Field, ModelField, ArrayField, ConditionalField
from .DroneData import DroneData
from .LocalLogisticOrder import LocalLogisticOrder
from .ShipData import ShipData
from .RemoteLogisticOrder import RemoteLogisticOrder
from .StationStore import StationStore


"""
StationComponent
{
    int32 version = 2
    int32 id
    int32 gid
    int32 entityId
    int32 planetId
    int32 pcId
    int32 gene
    float droneDock_x
    float droneDock_y
    float droneDock_z
    float shipDockPos_x
    float shipDockPos_y
    float shipDockPos_z
    float shipDockRot_x
    float shipDockRot_y
    float shipDockRot_z
    float shipDockRot_w
    uint8_bool isStellar
    int32 nameIsIncludedFlag (0 or 1)
    string name (nameIsIncludedFlag > 0)
    int64 energy
    int64 energyPerTick
    int64 energyMax
    int32 warperCount
    int32 warperMaxCount
    int32 idleDroneCount
    int32 workDroneCount
    int32: Used for allocating array sizes for workDroneDatas and workDroneOrders, and not uses for read in the arrays.
    DroneData workDroneDatas[workDroneCount]
    LocalLogisticOrder workDroneOrders[workDroneCount]
    int32 idleShipCount
    int32 workShipCount
    uint64 idleShipIndices
    uint64 workShipIndices
    int32: Used for allocating array sizes for workShipDatas, shipRenderers, shipUIRenderers, workShipOrders, and not uses for read in the arrays.
    ShipData workShipDatas[workShipCount]
    RemoteLogisticOrder workShipOrders[workShipCount]
    int32 numStorage
    StationStore[numStorage]
    (version >= 1) {
        int32 numSlots
        slots[numSlots] {
            int32 dir
            int32 beltId
            int32 storageIdx
            int32 counter
        }
    }
    int32 localPairProcess
    int32 remotePairProcess
    int32 nextShipIndex
    uint8_bool isCollector
    int32 numCollectionIds
    int32 collectionIds[numCollectionIds]
    int32 numCollectionPerTick
    float collectionPerTick[numCollectionPerTick]
    int32 numCurrentCollections
    float currentCollections[numCurrentCollections]
    int32 collectSpeed
    double tripRangeDrones (version >= 2)
    double tripRangeShips (version >= 2)
    uint8_bool includeOrbitCollector (version >= 2)
    double warpEnableDist (version >= 2)
    uint8_bool warperNecessary (version >= 2)
    int32 deliveryDrones (version >= 2)
    int32 deliveryShips (version >= 2)
}
"""


class Slot(Model):
    dir = Int32Field()
    beltId = Int32Field()
    storageIdx = Int32Field()
    counter = Int32Field()


class StationComponent(Model):
    version = Int32Field()
    id = Int32Field()
    gid = Int32Field()
    entityId = Int32Field()
    planetId = Int32Field()
    pcId = Int32Field()
    gene = Int32Field()
    droneDock_x = FloatField()
    droneDock_y = FloatField()
    droneDock_z = FloatField()
    shipDockPos_x = FloatField()
    shipDockPos_y = FloatField()
    shipDockPos_z = FloatField()
    shipDockRot_x = FloatField()
    shipDockRot_y = FloatField()
    shipDockRot_z = FloatField()
    shipDockRot_w = FloatField()
    isStellar = BoolField()
    nameIsIncludedFlag = Int32Field()
    name = ConditionalField(StringField, arg_fields='nameIsIncludedFlag', condition_func=g(0))
    energy = Int64Field()
    energyPerTick = Int64Field()
    energyMax = Int64Field()
    warperCount = Int32Field()
    warperMaxCount = Int32Field()
    idleDroneCount = Int32Field()
    workDroneCount = Int32Field()
    unused1 = Int32Field()
    workDroneDatas = ArrayField(lambda: ModelField(DroneData), length_field='workDroneCount')
    workDroneOrders = ArrayField(lambda: ModelField(LocalLogisticOrder), length_field='workDroneCount')
    idleShipCount = Int32Field()
    workShipCount = Int32Field()
    idleShipIndices = UInt64Field()
    workShipIndices = UInt64Field()
    unused2 = Int32Field()
    workShipDatas = ArrayField(lambda: ModelField(ShipData), length_field='workShipCount')
    workShipOrders = ArrayField(lambda: ModelField(RemoteLogisticOrder), length_field='workShipCount')
    numStorage = ArrayField(lambda: ModelField(StationStore))
    slots = ConditionalField(lambda: ArrayField(lambda: ModelField(Slot)), arg_fields='version', condition_func=ge(1))
    localPairProcess = Int32Field()
    remotePairProcess = Int32Field()
    nextShipIndex = Int32Field()
    isCollector = BoolField()
    collectionIds = ArrayField(Int32Field)
    collectionPerTick = ArrayField(FloatField)
    currentCollections = ArrayField(FloatField)
    collectSpeed = Int32Field()
    versionCheck = ConditionalBlockStart('version', ge(2))
    tripRangeDrones = DoubleField()
    tripRangeShips = DoubleField()
    includeOrbitCollector = BoolField()
    warpEnableDist = DoubleField()
    warperNecessary = BoolField()
    deliveryDrones = Int32Field()
    deliveryShips = Int32Field()
