from Field import Int32Field, FloatField, DoubleField, ReaderField, ArrayField
from Reader import Reader
from Readers.StorageComponent import StorageComponent
from Readers.MechaForge import MechaForge
from Readers.MechaLab import MechaLab
from Readers.MechaDrone import MechaDrone


"""
Mecha
{
    int32 version = 0
    double coreEnergyCap
    double coreEnergy
    double corePowerGen
    double reactorPowerGen
    double reactorEnergy
    int32 reactorItemId
    StorageComponent reactorStorage
    StorageComponent warpStorage
    double walkPower
    double jumpEnergy
    double thrustPowerPerAcc
    double warpKeepingPowerPerSpeed
    double warpStartPowerPerSpeed
    double miningPower
    double replicatePower
    double researchPower
    double droneEjectEnergy
    double droneEnergyPerMeter
    int32 coreLevel
    int32 thrusterLevel
    float miningSpeed
    float replicateSpeed
    float walkSpeed
    float jumpSpeed
    float maxSailSpeed
    float maxWarpSpeed
    float buildArea
    MechaForge
    MechaLab
    int32 droneCount
    float droneSpeed
    int32 droneMovement
    MechaDrone[droneCount]
}
"""


class Mecha(Reader):
    version = Int32Field()
    coreEnergyCap = DoubleField()
    coreEnergy = DoubleField()
    corePowerGen = DoubleField()
    reactorPowerGen = DoubleField()
    reactorEnergy = DoubleField()
    reactorItemId = Int32Field()
    reactorStorage = ReaderField(StorageComponent)
    warpStorage = ReaderField(StorageComponent)
    walkPower = DoubleField()
    jumpEnergy = DoubleField()
    thrustPowerPerAcc = DoubleField()
    warpKeepingPowerPerSpeed = DoubleField()
    warpStartPowerPerSpeed = DoubleField()
    miningPower = DoubleField()
    replicatePower = DoubleField()
    researchPower = DoubleField()
    droneEjectEnergy = DoubleField()
    droneEnergyPerMeter = DoubleField()
    coreLevel = Int32Field()
    thrusterLevel = Int32Field()
    miningSpeed = FloatField()
    replicateSpeed = FloatField()
    walkSpeed = FloatField()
    jumpSpeed = FloatField()
    maxSailSpeed = FloatField()
    maxWarpSpeed = FloatField()
    buildArea = FloatField()
    mechaForge = ReaderField(MechaForge)
    mechaLab = ReaderField(MechaLab)
    droneCount = Int32Field()
    droneSpeed = FloatField()
    droneMovement = Int32Field()
    mechaDrones = ArrayField(lambda: ReaderField(MechaDrone), length_field='droneCount')
