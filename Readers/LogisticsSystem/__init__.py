from Field import Int32Field, ReaderField, ArrayField, ConditionalField
from Func import ne, decr
from Reader import Reader
from Readers.LogisticsSystem.StationComponent import StationComponent


"""
PlanetTransport
{
    int32 version = 0
    int32 stationCursor
    int32 stationCapacity
    int32 stationRecycleCursor
    [stationCursor - 1] {
        int32 stationIndex
        StationComponent stationPool (stationIndex != 0)
    }
    int32 stationRecycle[stationRecycleCursor]
}
"""


class StationComponentSwitch(Reader):
    stationIndex = Int32Field()
    stationPool = ConditionalField(lambda: ReaderField(StationComponent),
                                   arg_fields='stationIndex', condition_func=ne(0))


class PlanetTransport(Reader):
    version = Int32Field()
    stationCursor = Int32Field()
    stationCapacity = Int32Field()
    stationRecycleCursor = Int32Field()
    stationPool = ArrayField(lambda: ReaderField(StationComponentSwitch),
                             length_field='stationCursor', length_function=decr())
    stationRecycle = ArrayField(Int32Field, length_field='stationRecycleCursor')
