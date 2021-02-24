from . import Model, Int32Field, FloatField


class MechaDrone(Model):
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
