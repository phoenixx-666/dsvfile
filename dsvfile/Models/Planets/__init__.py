from ...Fields import UInt32Field, FloatField, ArrayField, ModelField, ConditionalField
from ...Func import ge, decr, decrmul
from .. import Model, Int32Field
from .PlanetData import PlanetData
from .EntityData import EntityData
from .PrebuildData import PrebuildData
from .VegeData import VegeData
from .VeinData import VeinData
from ..CargoContainer import CargoContainer
from ..CargoTraffic import CargoTraffic
from ..StorageSystem import FactoryStorage
from ..PowerSystem import PowerSystem
from ..FactorySystem import FactorySystem
from ..LogisticsSystem import PlanetTransport
from ..MonsterSystem import MonsterSystem
from ..PlatformSystem import PlatformSystem


class Anim(Model):
    time = FloatField()
    prepare_length = FloatField()
    working_length = FloatField()
    state = UInt32Field()
    power = FloatField()


class EntitySign(Model):
    signType = UInt32Field()
    iconType = UInt32Field()
    iconId0 = UInt32Field()
    iconId1 = UInt32Field()
    iconId2 = UInt32Field()
    iconId3 = UInt32Field()
    count0 = FloatField()
    count1 = FloatField()
    count2 = FloatField()
    count3 = FloatField()
    x = FloatField()
    y = FloatField()
    z = FloatField()
    w = FloatField()


class PlanetFactory(Model):
    version = Int32Field()
    planetId = Int32Field()
    planetData = ModelField(PlanetData)
    entityCapacity = Int32Field()
    entityCursor = Int32Field()
    entityRecycleCursor = Int32Field()
    entityPool = ArrayField(ModelField(EntityData), length_field='entityCursor', length_func=decr())
    entityAnimPool = ArrayField(ModelField(Anim), length_field='entityCursor', length_func=decr())
    entitySignPool = ArrayField(ModelField(EntitySign), length_field='entityCursor', length_func=decr())
    entityConnPool = ArrayField(Int32Field, length_field='entityCursor', length_func=decrmul(16))
    entityRecycle = ArrayField(Int32Field, length_field='entityRecycleCursor')
    prebuildCapacity = Int32Field()
    prebuildCursor = Int32Field()
    prebuildRecycleCursor = Int32Field()
    prebuildPool = ArrayField(ModelField(PrebuildData), length_field='prebuildCursor', length_func=decr())
    prebuildConnPool = ArrayField(Int32Field, length_field='prebuildCursor', length_func=decrmul(16))
    prebuildRecycle = ArrayField(Int32Field, length_field='prebuildRecycleCursor')
    vegeCapacity = Int32Field()
    vegeCursor = Int32Field()
    vegeRecycleCursor = Int32Field()
    vegePool = ArrayField(ModelField(VegeData), length_field='vegeCursor', length_func=decr())
    vegeRecycle = ArrayField(Int32Field, length_field='vegeRecycleCursor')
    veinCapacity = Int32Field()
    veinCursor = Int32Field()
    veinRecycleCursor = Int32Field()
    veinPool = ArrayField(ModelField(VeinData), length_field='veinCursor', length_func=decr())
    veinRecycle = ArrayField(Int32Field, length_field='veinRecycleCursor')
    veinAnimPool = ArrayField(ModelField(Anim), length_field='veinCursor', length_func=decr())
    cargoContainer = ModelField(CargoContainer)
    cargoTraffic = ModelField(CargoTraffic)
    factoryStorage = ModelField(FactoryStorage)
    powerSystem = ModelField(PowerSystem)
    factorySystem = ModelField(FactorySystem)
    planetTransport = ModelField(PlanetTransport)
    monsterSystem = ModelField(MonsterSystem)
    platformSystem = ConditionalField(ModelField(PlatformSystem), arg_fields='version', condition_func=ge(1))
