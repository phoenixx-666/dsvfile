from ...Fields import ModelField, ArrayField
from ...Func import decr
from .. import Model, Int32Field
from .MinerComponent import MinerComponent
from .InserterComponent import InserterComponent
from .AssemblerComponent import AssemblerComponent
from .FractionateComponent import FractionateComponent
from .EjectorComponent import EjectorComponent
from .SiloComponent import SiloComponent
from .LabComponent import LabComponent


class FactorySystem(Model):
    version = Int32Field()
    minerCapacity = Int32Field()
    minerCursor = Int32Field()
    minerRecycleCursor = Int32Field()
    minerPool = ArrayField(lambda: ModelField(MinerComponent), length_field='minerCursor', length_func=decr())
    minerRecycle = ArrayField(Int32Field, length_field='minerRecycleCursor')
    inserterCapacity = Int32Field()
    inserterCursor = Int32Field()
    inserterRecycleCursor = Int32Field()
    inserterPool = ArrayField(lambda: ModelField(InserterComponent),
                              length_field='inserterCursor', length_func=decr())
    inserterRecycle = ArrayField(Int32Field, length_field='inserterRecycleCursor')
    assemblerCapacity = Int32Field()
    assemblerCursor = Int32Field()
    assemblerRecycleCursor = Int32Field()
    assemblerPool = ArrayField(lambda: ModelField(AssemblerComponent),
                               length_field='assemblerCursor', length_func=decr())
    assemblerRecycle = ArrayField(Int32Field, length_field='assemblerRecycleCursor')
    fractionateCapacity = Int32Field()
    fractionateCursor = Int32Field()
    fractionateRecycleCursor = Int32Field()
    fractionatePool = ArrayField(lambda: ModelField(FractionateComponent),
                                 length_field='fractionateCursor', length_func=decr())
    fractionateRecycle = ArrayField(Int32Field, length_field='fractionateRecycleCursor')
    ejectorCapacity = Int32Field()
    ejectorCursor = Int32Field()
    ejectorRecycleCursor = Int32Field()
    ejectorPool = ArrayField(lambda: ModelField(EjectorComponent),
                             length_field='ejectorCursor', length_func=decr())
    ejectorRecycle = ArrayField(Int32Field, length_field='ejectorRecycleCursor')
    siloCapacity = Int32Field()
    siloCursor = Int32Field()
    siloRecycleCursor = Int32Field()
    siloPool = ArrayField(lambda: ModelField(SiloComponent), length_field='siloCursor', length_func=decr())
    siloRecycle = ArrayField(Int32Field, length_field='siloRecycleCursor')
    labCapacity = Int32Field()
    labCursor = Int32Field()
    labRecycleCursor = Int32Field()
    labPool = ArrayField(lambda: ModelField(LabComponent), length_field='labCursor', length_func=decr())
    labRecycle = ArrayField(Int32Field, length_field='labRecycleCursor')
