from ...Fields import ModelField, ArrayField, ConditionalField
from ...Func import ne, decr
from .. import Model, Int32Field
from .StationComponent import StationComponent


class StationComponentSwitch(Model):
    stationIndex = Int32Field()
    stationPool = ConditionalField(ModelField(StationComponent), arg_fields='stationIndex', condition_func=ne(0))


class PlanetTransport(Model):
    version = Int32Field()
    stationCursor = Int32Field()
    stationCapacity = Int32Field()
    stationRecycleCursor = Int32Field()
    stationPool = ArrayField(ModelField(StationComponentSwitch), length_field='stationCursor', length_func=decr())
    stationRecycle = ArrayField(Int32Field, length_field='stationRecycleCursor')
