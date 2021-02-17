from Field import Int32Field, ReaderField, ArrayField, ConditionalField
from Func import ne, decr
from Reader import Reader
from Readers.CargoTraffic.BeltComponent import BeltComponent
from Readers.CargoTraffic.SplitterComponent import SplitterComponent
from Readers.CargoTraffic.CargoPath import CargoPath


"""
CargoTraffic
{
    int32 version = 0
    int32 beltCursor
    int32 beltCapacity
    int32 beltRecycleCursor
    int32 splitterCursor
    int32 splitterCapacity
    int32 splitterRecycleCursor
    int32 pathCursor
    int32 pathCapacity
    int32 pathRecycleCursor
    BeltComponent beltPool[beltCursor - 1]
    int32 beltRecycle[beltRecycleCursor]
    SplitterComponent splitterPool[splitterCursor - 1]
    int32 splitterRecycle[splitterRecycleCursor]
    [pathCursor - 1] {
        int32 cargoPathIndex
        CargoPath pathPool (cargoPathIndex != 0)
    }
    int32 pathRecycle[pathRecycleCursor]
}
"""


class CargoPathSwitch(Reader):
    cargoPathIndex = Int32Field()
    pathPool = ConditionalField(lambda: ReaderField(CargoPath), arg_fields='cargoPathIndex', condition_func=ne(0))


class CargoTraffic(Reader):
    version = Int32Field()
    beltCursor = Int32Field()
    beltCapacity = Int32Field()
    beltRecycleCursor = Int32Field()
    splitterCursor = Int32Field()
    splitterCapacity = Int32Field()
    splitterRecycleCursor = Int32Field()
    pathCursor = Int32Field()
    pathCapacity = Int32Field()
    pathRecycleCursor = Int32Field()
    beltPool = ArrayField(lambda: ReaderField(BeltComponent), length_field='beltCursor', length_function=decr())
    beltRecycle = ArrayField(Int32Field, length_field='beltRecycleCursor')
    splitterPool = ArrayField(lambda: ReaderField(SplitterComponent),
                              length_field='splitterCursor', length_function=decr())
    splitterRecycle = ArrayField(Int32Field, length_field='splitterRecycleCursor')
    pathPool = ArrayField(lambda: ReaderField(CargoPathSwitch), length_field='pathCursor', length_function=decr())
    pathRecycle = ArrayField(Int32Field, length_field='pathRecycleCursor')
