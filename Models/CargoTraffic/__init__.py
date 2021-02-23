from Fields import Int32Field, ModelField, ArrayField, ConditionalField
from Func import ne, decr
from Models import Model
from Models.CargoTraffic.BeltComponent import BeltComponent
from Models.CargoTraffic.SplitterComponent import SplitterComponent
from Models.CargoTraffic.CargoPath import CargoPath


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


class CargoPathSwitch(Model):
    cargoPathIndex = Int32Field()
    pathPool = ConditionalField(lambda: ModelField(CargoPath), arg_fields='cargoPathIndex', condition_func=ne(0))


class CargoTraffic(Model):
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
    beltPool = ArrayField(lambda: ModelField(BeltComponent), length_field='beltCursor', length_func=decr())
    beltRecycle = ArrayField(Int32Field, length_field='beltRecycleCursor')
    splitterPool = ArrayField(lambda: ModelField(SplitterComponent),
                              length_field='splitterCursor', length_func=decr())
    splitterRecycle = ArrayField(Int32Field, length_field='splitterRecycleCursor')
    pathPool = ArrayField(lambda: ModelField(CargoPathSwitch), length_field='pathCursor', length_func=decr())
    pathRecycle = ArrayField(Int32Field, length_field='pathRecycleCursor')
