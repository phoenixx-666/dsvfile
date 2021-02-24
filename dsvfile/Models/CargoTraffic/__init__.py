from ...Fields import ModelField, ArrayField, ConditionalField
from ...Func import ne, decr
from .. import Model, Int32Field
from .BeltComponent import BeltComponent
from .SplitterComponent import SplitterComponent
from .CargoPath import CargoPath


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
