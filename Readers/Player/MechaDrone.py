from Field import Int32Field, FloatField
from Reader import Reader


"""
MechaDrone
{
    int32 version = 0
    int32 stage
    float position_x
    float position_y
    float position_z
    float target_x
    float target_y
    float target_z
    float forward_x
    float forward_y
    float forward_z
    float speed
    int32 movement
    int32 targetObject
    float progress
    float initialVector_x
    float initialVector_y
    float initialVector_z
}
"""


class MechaDrone(Reader):
    version = Int32Field()
    stage = Int32Field()
    position_x = FloatField()
    position_y = FloatField()
    position_z = FloatField()
    target_x = FloatField()
    target_y = FloatField()
    target_z = FloatField()
    forward_x = FloatField()
    forward_y = FloatField()
    forward_z = FloatField()
    speed = FloatField()
    movement = Int32Field()
    targetObject = Int32Field()
    progress = FloatField()
    initialVector_x = FloatField()
    initialVector_y = FloatField()
    initialVector_z = FloatField()
