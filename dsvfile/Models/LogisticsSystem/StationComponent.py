from ...Fields import Int64Field, UInt64Field, FloatField, DoubleField, StringField, BoolField, ConditionalBlockStart
from ...Func import g, ge
from . import Model, Int32Field, ModelField, ArrayField, ConditionalField
from .DroneData import DroneData
from .LocalLogisticOrder import LocalLogisticOrder
from .ShipData import ShipData
from .RemoteLogisticOrder import RemoteLogisticOrder
from .StationStore import StationStore


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
