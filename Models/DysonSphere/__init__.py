from Fields import Int32Field, ModelField, ArrayField, ConditionalField, ConditionalBlockStart, ConditionalBlockEnd
from Func import g, ge, ne, eq, decr
from Models import Model
from Models.DysonSphere.DysonSwarm import DysonSwarm
from Models.DysonSphere.DysonSphereLayer import DysonSphereLayer
from Models.DysonSphere.DysonRocket import DysonRocket
from Models.DysonSphere.DysonNodeRData import DysonNodeRData


"""
DysonSphere
{
    int32 version = 2
    (version >= 1) {
        int32 randSeed
        DysonSwarm
        int32 = 1212: File will be rejected if the value is not 1212
        int32 layerCount
        int32 numDysonSphereLayer
        [numDysonSphereLayer - 1] {
            int32 dysonSphereLayerIndex
            DysonSphereLayer (dysonSphereLayerIndex != 0)
        }
        int32 rocketCapacity
        int32 rocketCursor
        int32 rocketRecycleCursor
        DysonRocket rocketPool[rocketCursor - 1]
        int32 rocketRecycle[rocketRecycleCursor]
        int32 autoNodeCount
        int32 numAutoNodes
        [numAutoNodes] {
            int32 autoNodeIncludedFlag
            int32 layerId (autoNodeIncludedFlag > 0)
            int32 nodeId (autoNodeIncludedFlag > 0)
        }
    }
    (version >= 2) {
        int32 nrdCapacity
        int32 nrdCursor
        int32 nrdRecycleCursor
        DysonNodeRData nrdPool[nrdCursor]
        int32 nrdRecycle[nrdRecycleCursor]
    }
}
"""


class DysonSphereLayerSwitch(Model):
    dysonSphereLayerIndex = Int32Field()
    dysonSphereLayer = ConditionalField(lambda: ModelField(DysonSphereLayer),
                                        arg_fields='dysonSphereLayerIndex', condition_func=ne(0))


class AutoNode(Model):
    autoNodeIncludedFlag = Int32Field()
    layerId = ConditionalField(Int32Field, arg_fields='autoNodeIncludedFlag', condition_func=g(0))
    nodeId = ConditionalField(Int32Field, arg_fields='autoNodeIncludedFlag', condition_func=g(0))


class DysonSphere(Model):
    version = Int32Field()
    versionCheck1 = ConditionalBlockStart(arg_fields='version', condition_func=ge(1))
    randSeed = Int32Field()
    dysonSwarm = ModelField(DysonSwarm)
    eq1212 = Int32Field()
    layerCount = Int32Field()
    numDysonSphereLayer = Int32Field()
    dysonSphereLayers = ArrayField(lambda: ModelField(DysonSphereLayerSwitch),
                                   length_field='numDysonSphereLayer', length_func=decr())
    rocketCapacity = Int32Field()
    rocketCursor = Int32Field()
    rocketRecycleCursor = Int32Field()
    rocketPool = ArrayField(lambda: ModelField(DysonRocket), length_field='rocketCursor', length_func=decr())
    rocketRecycle = ArrayField(Int32Field, length_field='rocketRecycleCursor')
    autoNodeCount = Int32Field()
    numAutoNodes = Int32Field()
    autoNodes = ArrayField(lambda: ModelField(AutoNode), length_field='numAutoNodes')
    versionCheck2 = ConditionalBlockStart(arg_fields='version', condition_func=ge(2))
    nrdCapacity = Int32Field()
    nrdCursor = Int32Field()
    nrdRecycleCursor = Int32Field()
    nrdPool = ArrayField(lambda: ModelField(DysonNodeRData), length_field='nrdCursor', length_func=decr())
    nrdRecycle = ArrayField(Int32Field, length_field='nrdRecycleCursor')


class DysonSphereSwitch(Model):
    dysonSphereDataIsAvailableFlag = Int32Field()
    dysonSphere = ConditionalField(lambda: ModelField(DysonSphere),
                                   arg_fields='dysonSphereDataIsAvailableFlag', condition_func=eq(1))
