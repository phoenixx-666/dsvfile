from ...Fields import ModelField, ArrayField, ConditionalField, ConditionalBlockStart
from ...Func import g, ge, ne, eq, decr
from .. import Model, Int32Field
from .DysonSwarm import DysonSwarm
from .DysonSphereLayer import DysonSphereLayer
from .DysonRocket import DysonRocket
from .DysonNodeRData import DysonNodeRData


class DysonSphereLayerSwitch(Model):
    dysonSphereLayerIndex = Int32Field()
    dysonSphereLayer = ConditionalField(ModelField(DysonSphereLayer),
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
    dysonSphereLayers = ArrayField(ModelField(DysonSphereLayerSwitch),
                                   length_field='numDysonSphereLayer', length_func=decr())
    rocketCapacity = Int32Field()
    rocketCursor = Int32Field()
    rocketRecycleCursor = Int32Field()
    rocketPool = ArrayField(ModelField(DysonRocket), length_field='rocketCursor', length_func=decr())
    rocketRecycle = ArrayField(Int32Field, length_field='rocketRecycleCursor')
    autoNodeCount = Int32Field()
    numAutoNodes = Int32Field()
    autoNodes = ArrayField(ModelField(AutoNode), length_field='numAutoNodes')
    versionCheck2 = ConditionalBlockStart(arg_fields='version', condition_func=ge(2))
    nrdCapacity = Int32Field()
    nrdCursor = Int32Field()
    nrdRecycleCursor = Int32Field()
    nrdPool = ArrayField(ModelField(DysonNodeRData), length_field='nrdCursor', length_func=decr())
    nrdRecycle = ArrayField(Int32Field, length_field='nrdRecycleCursor')


class DysonSphereSwitch(Model):
    dysonSphereDataIsAvailableFlag = Int32Field()
    dysonSphere = ConditionalField(ModelField(DysonSphere),
                                   arg_fields='dysonSphereDataIsAvailableFlag', condition_func=eq(1))
