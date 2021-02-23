from ...Fields import FloatField
from ...Func import ne, decr
from . import Model, Int32Field, ModelField, ArrayField, ConditionalField
from .DysonNode import DysonNode
from .DysonFrame import DysonFrame
from .DysonShell import DysonShell


"""
DysonSphereLayer
{
    int32 version = 0
    int32 id
    float orbitRadius
    float orbitRotation_x
    float orbitRotation_y
    float orbitRotation_z
    float orbitRotation_w
    float orbitAngularSpeed
    float currentAngle
    float currentRotation_x
    float currentRotation_y
    float currentRotation_z
    float currentRotation_w
    float nextRotation_x
    float nextRotation_y
    float nextRotation_z
    float nextRotation_w
    int32 gridMode
    int32 nodeCapacity
    int32 nodeCursor
    int32 nodeRecycleCursor
    [nodeCursor - 1] {
        int32 dysonNodeIndex
        DysonNode (dysonNodeIndex != 0)
    }
    int32 nodeRecycle[nodeRecycleCursor]
    int32 frameCapacity
    int32 frameCursor
    int32 frameRecycleCursor
    [frameCursor - 1] {
        int32 dysonFrameIndex
        DysonFrame (dysonFrameIndex != 0)
    }
    int32 frameRecycle[frameRecycleCursor]
    int32 shellCapacity
    int32 shellCursor
    int32 shellRecycleCursor
    [shellCursor - 1] {
        int32 dysonShellIndex
        DysonShell (dysonShellIndex != 0)
    }
    int32 shellRecycle[shellRecycleCursor]
}
"""


class DysonNodeSwitch(Model):
    dysonNodeIndex = Int32Field()
    dysonNode = ConditionalField(lambda: ModelField(DysonNode), arg_fields='dysonNodeIndex', condition_func=ne(0))


class DysonFrameSwitch(Model):
    dysonFrameIndex = Int32Field()
    dysonFrame = ConditionalField(lambda: ModelField(DysonFrame), arg_fields='dysonFrameIndex', condition_func=ne(0))


class DysonShellSwitch(Model):
    dysonShellIndex = Int32Field()
    dysonShell = ConditionalField(lambda: ModelField(DysonShell), arg_fields='dysonShellIndex', condition_func=ne(0))


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
    nodes = ArrayField(lambda: ModelField(DysonNodeSwitch), length_field='nodeCursor', length_func=decr())
    nodeRecycle = ArrayField(Int32Field, length_field='nodeRecycleCursor')
    frameCapacity = Int32Field()
    frameCursor = Int32Field()
    frameRecycleCursor = Int32Field()
    frames = ArrayField(lambda: ModelField(DysonFrameSwitch), length_field='frameCursor', length_func=decr())
    frameRecycle = ArrayField(Int32Field, length_field='frameRecycleCursor')
    shellCapacity = Int32Field()
    shellCursor = Int32Field()
    shellRecycleCursor = Int32Field()
    shells = ArrayField(lambda: ModelField(DysonShellSwitch), length_field='shellCursor', length_func=decr())
    shellRecycle = ArrayField(Int32Field, length_field='shellRecycleCursor')
