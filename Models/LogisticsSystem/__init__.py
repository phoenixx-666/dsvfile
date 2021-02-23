from Fields import Int32Field, ModelField, ArrayField, ConditionalField
from Func import ne, decr
from Models import Model
from Models.LogisticsSystem.StationComponent import StationComponent


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


class StationComponentSwitch(Model):
    stationIndex = Int32Field()
    stationPool = ConditionalField(lambda: ModelField(StationComponent),
                                   arg_fields='stationIndex', condition_func=ne(0))


class PlanetTransport(Model):
    version = Int32Field()
    stationCursor = Int32Field()
    stationCapacity = Int32Field()
    stationRecycleCursor = Int32Field()
    stationPool = ArrayField(lambda: ModelField(StationComponentSwitch),
                             length_field='stationCursor', length_func=decr())
    stationRecycle = ArrayField(Int32Field, length_field='stationRecycleCursor')
