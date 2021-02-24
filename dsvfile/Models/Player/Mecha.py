from ...Fields import ArrayField
from . import Model, Int32Field, FloatField, DoubleField, ModelField
from ..StorageSystem.StorageComponent import StorageComponent
from .MechaForge import MechaForge
from .MechaLab import MechaLab
from .MechaDrone import MechaDrone


class Mecha(Model):
    version = Int32Field()
    coreEnergyCap = DoubleField()
    coreEnergy = DoubleField()
    corePowerGen = DoubleField()
    reactorPowerGen = DoubleField()
    reactorEnergy = DoubleField()
    reactorItemId = Int32Field()
    reactorStorage = ModelField(StorageComponent)
    warpStorage = ModelField(StorageComponent)
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
    mechaForge = ModelField(MechaForge)
    mechaLab = ModelField(MechaLab)
    droneCount = Int32Field()
    droneSpeed = FloatField()
    droneMovement = Int32Field()
    mechaDrones = ArrayField(lambda: ModelField(MechaDrone), length_field='droneCount')
