from ...Fields import FloatField, DoubleField, BoolField, ModelField
from ...Fields.Enums import EMovementState
from .. import Model, Int32Field
from .Mecha import Mecha
from ..StorageSystem.StorageComponent import StorageComponent
from .PlayerNavigation import PlayerNavigation


class Player(Model):
    version = Int32Field()
    planetId = Int32Field()
    position_x = FloatField()
    position_y = FloatField()
    position_z = FloatField()
    uPosition_x = DoubleField()
    uPosition_y = DoubleField()
    uPosition_z = DoubleField()
    uRotation_x = FloatField()
    uRotation_y = FloatField()
    uRotation_z = FloatField()
    uRotation_w = FloatField()
    movementState = EMovementState()
    warpState = FloatField()
    warpCommand = BoolField()
    uVelocity_x = DoubleField()
    uVelocity_y = DoubleField()
    uVelocity_z = DoubleField()
    inhandItemId = Int32Field()
    inhandItemCount = Int32Field()
    mecha = ModelField(Mecha)
    package = ModelField(StorageComponent)
    playerNavigation = ModelField(PlayerNavigation)
    sandCount = Int32Field()
