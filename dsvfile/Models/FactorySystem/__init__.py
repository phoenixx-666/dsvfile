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


"""
FactorySystem
{
    int32 version = 0
    int32 minerCapacity
    int32 minerCursor
    int32 minerRecycleCursor
    MinerComponent minerPool[minerCursor - 1]
    int32 minerRecycle[minerRecycleCursor]
    int32 inserterCapacity
    int32 inserterCursor
    int32 inserterRecycleCursor
    InserterComponent inserterPool[inserterCursor - 1]
    int32 inserterRecycle[inserterRecycleCursor]
    int32 assemblerCapacity
    int32 assemblerCursor
    int32 assemblerRecycleCursor
    AssemblerComponent assemblerPool[assemblerCursor - 1]
    int32 assemblerRecycle[assemblerRecycleCursor]
    int32 fractionateCapacity
    int32 fractionateCursor
    int32 fractionateRecycleCursor
    FractionateComponent fractionatePool[fractionateCursor - 1]
    int32 fractionateRecycle[fractionateRecycleCursor]
    int32 ejectorCapacity
    int32 ejectorCursor
    int32 ejectorRecycleCursor
    EjectorComponent ejectorPool[ejectorCursor - 1]
    int32 ejectorRecycle[ejectorRecycleCursor]
    int32 siloCapacity
    int32 siloCursor
    int32 siloRecycleCursor
    SiloComponent siloPool[siloCursor - 1]
    int32 siloRecycle[siloRecycleCursor]
    int32 labCapacity
    int32 labCursor
    int32 labRecycleCursor
    LabComponent labPool[labCursor - 1]
    int32 labRecycle[labRecycleCursor]
}
"""


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
