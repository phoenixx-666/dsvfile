from Fields import Int32Field, FloatField, DoubleField, BoolField, ModelField
from Fields.Enums import EMovementState
from Models import Model
from Models.Player.Mecha import Mecha
from Models.StorageSystem.StorageComponent import StorageComponent
from Models.Player.PlayerNavigation import PlayerNavigation


"""
Player
{
    int32 version = 1
    int32 planetId: Ignored on read
    float position_x
    float position_y
    float position_z
    double uPosition_x
    double uPosition_y
    double uPosition_z
    float uRotation_x
    float uRotation_y
    float uRotation_z
    float uRotation_w
    int32 EMovementState movementState (Walk, Drift, Fly, Sail)
    float warpState
    uint8_bool warpCommand
    double uVelocity_x
    double uVelocity_y
    double uVelocity_z
    int32 inhandItemId
    int32 inhandItemCount
    Mecha
    StorageComponent package
    PlayerNavigation
    int32 sandCount
}
"""


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
