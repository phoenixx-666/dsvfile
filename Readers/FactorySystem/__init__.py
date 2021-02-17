from Field import Int32Field, ReaderField, ArrayField
from Func import decr
from Reader import Reader
from Readers.FactorySystem.MinerComponent import MinerComponent
from Readers.FactorySystem.InserterComponent import InserterComponent
from Readers.FactorySystem.AssemblerComponent import AssemblerComponent
from Readers.FactorySystem.FractionateComponent import FractionateComponent
from Readers.FactorySystem.EjectorComponent import EjectorComponent
from Readers.FactorySystem.SiloComponent import SiloComponent
from Readers.FactorySystem.LabComponent import LabComponent


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


class FactorySystem(Reader):
    version = Int32Field()
    minerCapacity = Int32Field()
    minerCursor = Int32Field()
    minerRecycleCursor = Int32Field()
    minerPool = ArrayField(lambda: ReaderField(MinerComponent), length_field='minerCursor', length_function=decr())
    minerRecycle = ArrayField(Int32Field, length_field='minerRecycleCursor')
    inserterCapacity = Int32Field()
    inserterCursor = Int32Field()
    inserterRecycleCursor = Int32Field()
    inserterPool = ArrayField(lambda: ReaderField(InserterComponent),
                              length_field='inserterCursor', length_function=decr())
    inserterRecycle = ArrayField(Int32Field, length_field='inserterRecycleCursor')
    assemblerCapacity = Int32Field()
    assemblerCursor = Int32Field()
    assemblerRecycleCursor = Int32Field()
    assemblerPool = ArrayField(lambda: ReaderField(AssemblerComponent),
                               length_field='assemblerCursor', length_function=decr())
    assemblerRecycle = ArrayField(Int32Field, length_field='assemblerRecycleCursor')
    fractionateCapacity = Int32Field()
    fractionateCursor = Int32Field()
    fractionateRecycleCursor = Int32Field()
    fractionatePool = ArrayField(lambda: ReaderField(FractionateComponent),
                                 length_field='fractionateCursor', length_function=decr())
    fractionateRecycle = ArrayField(Int32Field, length_field='fractionateRecycleCursor')
    ejectorCapacity = Int32Field()
    ejectorCursor = Int32Field()
    ejectorRecycleCursor = Int32Field()
    ejectorPool = ArrayField(lambda: ReaderField(EjectorComponent),
                             length_field='ejectorCursor', length_function=decr())
    ejectorRecycle = ArrayField(Int32Field, length_field='ejectorRecycleCursor')
    siloCapacity = Int32Field()
    siloCursor = Int32Field()
    siloRecycleCursor = Int32Field()
    siloPool = ArrayField(lambda: ReaderField(SiloComponent), length_field='siloCursor', length_function=decr())
    siloRecycle = ArrayField(Int32Field, length_field='siloRecycleCursor')
    labCapacity = Int32Field()
    labCursor = Int32Field()
    labRecycleCursor = Int32Field()
    labPool = ArrayField(lambda: ReaderField(LabComponent), length_field='labCursor', length_function=decr())
    labRecycle = ArrayField(Int32Field, length_field='labRecycleCursor')
