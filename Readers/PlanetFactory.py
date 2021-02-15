from Field import Int32Field, UInt32Field, FloatField, ArrayField, ReaderField
from Reader import Reader
from Readers.PlanetData import PlanetData
from Readers.EntityData import EntityData
from Readers.PrebuildData import PrebuildData
from Readers.VegeData import VegeData
from Readers.VeinData import VeinData

"""
PlanetFactory
{
    int32 version = 1
    int32 planetId
    PlanetData
    int32 entityCapacity
    int32 entityCursor
    int32 entityRecycleCursor
    EntityData entityPool[entityCursor - 1]
    entityAnimPool[entityCursor - 1] {
        float time
        float prepare_length
        float working_length
        uint32 state
        float power
    }
    entitySignPool[entityCursor - 1] {
        uint32 signType
        uint32 iconType
        uint32 iconId0
        uint32 iconId1
        uint32 iconId2
        uint32 iconId3
        float count0
        float count1
        float count2
        float count3
        float x
        float y
        float z
        float w
    }
    int32 entityConnPool[entityCursor * 16 - 16]
    int32 entityRecycle[entityRecycleCursor]
    int32 prebuildCapacity
    int32 prebuildCursor
    int32 prebuildRecycleCursor
    PrebuildData prebuildPool[prebuildCursor - 1]
    int32 prebuildConnPool[prebuildCursor * 16 - 16]
    int32 prebuildRecycle[prebuildRecycleCursor]
    int32 vegeCapacity
    int32 vegeCursor
    int32 vegeRecycleCursor
    VegeData vegePool[vegeCursor - 1]
    int32 vegeRecycle[vegeRecycleCursor]
    int32 veinCapacity
    int32 veinCursor
    int32 veinRecycleCursor
    VeinData veinPool[veinCursor - 1]
    int32 veinRecycle[veinRecycleCursor]
    veinAnimPool[veinCursor - 1] {
        float time
        float prepare_length
        float working_length
        uint32 state
        float power
    }
    CargoContainer
    CargoTraffic
    FactoryStorage
    PowerSystem
    FactorySystem
    PlanetTransport
    MonsterSystem
    PlatformSystem (version >= 1)
}
"""


class EntityAnim(Reader):
    time = FloatField()
    prepare_length = FloatField()
    working_length = FloatField()
    state = UInt32Field()
    power = FloatField()


class EntitySign(Reader):
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


class VeinAnim(Reader):
    time = FloatField()
    prepare_length = FloatField()
    working_length = FloatField()
    state = UInt32Field()
    power = FloatField()


class PlanetFactory(Reader):
    version = Int32Field()
    planetId = Int32Field()
    planetData = ReaderField(PlanetData)
    entityCapacity = Int32Field()
    entityCursor = Int32Field()
    entityRecycleCursor = Int32Field()
    entityPool = ArrayField(lambda: ReaderField(EntityData), length_field='entityCursor',
                            length_function=lambda x: x - 1)
    entityAnimPool = ArrayField(lambda: ReaderField(EntityAnim), length_field='entityCursor',
                                length_function=lambda x: x - 1)
    entitySignPool = ArrayField(lambda: ReaderField(EntitySign), length_field='entityCursor',
                                length_function=lambda x: x - 1)
    entityConnPool = ArrayField(Int32Field, length_field='entityCursor', length_function=lambda x: x * 16 - 16)
    entityRecycle = ArrayField(Int32Field, length_field='entityRecycleCursor')
    prebuildCapacity = Int32Field()
    prebuildCursor = Int32Field()
    prebuildRecycleCursor = Int32Field()
    prebuildPool = ArrayField(lambda: ReaderField(PrebuildData), length_field='prebuildCursor',
                              length_function=lambda x: x - 1)
    prebuildConnPool = ArrayField(Int32Field, length_field='prebuildCursor', length_function=lambda x: x * 16 - 16)
    prebuildRecycle = ArrayField(Int32Field, length_field='prebuildRecycleCursor')
    vegeCapacity = Int32Field()
    vegeCursor = Int32Field()
    vegeRecycleCursor = Int32Field()
    vegePool = ArrayField(lambda: ReaderField(VegeData), length_field='vegeCursor', length_function=lambda x: x - 1)
    vegeRecycle = ArrayField(Int32Field, length_field='vegeRecycleCursor')
    veinCapacity = Int32Field()
    veinCursor = Int32Field()
    veinRecycleCursor = Int32Field()
    veinPool = ArrayField(lambda: ReaderField(VeinData), length_field='veinCursor', length_function=lambda x: x - 1)
    veinRecycle = ArrayField(Int32Field, length_field='veinRecycleCursor')
    veinAnimPool = ArrayField(lambda: ReaderField(VeinAnim), length_field='veinCursor', length_function=lambda x: x - 1)
    """
    cargoContainer = ReaderField(CargoContainer)
    cargoTraffic = ReaderField(CargoTraffic)
    factoryStorage = ReaderField(FactoryStorage)
    powerSystem = ReaderField(PowerSystem)
    factorySystem = ReaderField(FactorySystem)
    planetTransport = ReaderField(PlanetTransport)
    monsterSystem = ReaderField(MonsterSystem)
    platformSystem = ReaderField(PlatformSystem)
    """