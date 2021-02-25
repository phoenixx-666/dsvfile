from ...Fields import FloatField
from ...Func import ne, decr
from . import Model, Int32Field, ModelField, ArrayField, ConditionalField
from .DysonNode import DysonNode
from .DysonFrame import DysonFrame
from .DysonShell import DysonShell


class DysonNodeSwitch(Model):
    dysonNodeIndex = Int32Field()
    dysonNode = ConditionalField(ModelField(DysonNode), arg_fields='dysonNodeIndex', condition_func=ne(0))


class DysonFrameSwitch(Model):
    dysonFrameIndex = Int32Field()
    dysonFrame = ConditionalField(ModelField(DysonFrame), arg_fields='dysonFrameIndex', condition_func=ne(0))


class DysonShellSwitch(Model):
    dysonShellIndex = Int32Field()
    dysonShell = ConditionalField(ModelField(DysonShell), arg_fields='dysonShellIndex', condition_func=ne(0))


class DysonSphereLayer(Model):
    version = Int32Field()
    id = Int32Field()
    orbitRadius = FloatField()
    orbitRotation_x = FloatField()
    orbitRotation_y = FloatField()
    orbitRotation_z = FloatField()
    orbitRotation_w = FloatField()
    orbitAngularSpeed = FloatField()
    currentAngle = FloatField()
    currentRotation_x = FloatField()
    currentRotation_y = FloatField()
    currentRotation_z = FloatField()
    currentRotation_w = FloatField()
    nextRotation_x = FloatField()
    nextRotation_y = FloatField()
    nextRotation_z = FloatField()
    nextRotation_w = FloatField()
    gridMode = Int32Field()
    nodeCapacity = Int32Field()
    nodeCursor = Int32Field()
    nodeRecycleCursor = Int32Field()
    nodes = ArrayField(ModelField(DysonNodeSwitch), length_field='nodeCursor', length_func=decr())
    nodeRecycle = ArrayField(Int32Field, length_field='nodeRecycleCursor')
    frameCapacity = Int32Field()
    frameCursor = Int32Field()
    frameRecycleCursor = Int32Field()
    frames = ArrayField(ModelField(DysonFrameSwitch), length_field='frameCursor', length_func=decr())
    frameRecycle = ArrayField(Int32Field, length_field='frameRecycleCursor')
    shellCapacity = Int32Field()
    shellCursor = Int32Field()
    shellRecycleCursor = Int32Field()
    shells = ArrayField(ModelField(DysonShellSwitch), length_field='shellCursor', length_func=decr())
    shellRecycle = ArrayField(Int32Field, length_field='shellRecycleCursor')
