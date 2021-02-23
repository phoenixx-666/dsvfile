from Fields import Int32Field, UInt32Field, Int64Field, FloatField, ModelField, ArrayField, ConditionalBlockStart
from Func import ge, decr
from Models import Model
from Models.DysonSphere.SailOrbit import SailOrbit
from Models.DysonSphere.SailBullet import SailBullet


"""
DysonSwarm
{
    int32 version = 4
    (version >= 1) {
        int32 randSeed
        int32 sailCapacity
        int32 sailCursor
        int32 sailRecycleCursor
        sailPoolForSave[sailCursor] {
            float st
            float px
            float py
            float pz
            float vx
            float vy
            float vz
            float gs
        }
        sailInfos[sailCursor] {
            uint32 orbit
            uint32 node (version >= 3)
            uint32 kill (version >= 3)
            float posr_x (version >= 4)
            float posr_y (version >= 4)
            float posr_z (version >= 4)
        }
        int32 sailRecycle[sailRecycleCursor]
        int32 orbitCapacity
        int32 orbitCursor
        SailOrbit orbits[orbitCursor - 1]
        int32 numExpiryOrder: Must match sailCapacity or the game will crash.
        int32 expiryCursor
        int32 expiryEnding
        [numExpiryOrder] {
            int64 time
            int32 index
        }
        (version >= 2) {
            int32 numAbsorbOrder: Must match sailCapacity or the game will crash.
            int32 absorbCursor
            int32 absorbEnding
            absorbOrder[numAbsorbOrder] {
                int64 time
                int32 index
                int32 layer
                int32 node
            }
        }
        int32 bulletCapacity
        int32 bulletCursor
        int32 bulletRecycleCursor
        SailBullet bulletPool[bulletCursor - 1]
        int32 bulletRecycle[bulletRecycleCursor]
    }
}
"""


class Sail(Model):
    st = FloatField()
    px = FloatField()
    py = FloatField()
    pz = FloatField()
    vx = FloatField()
    vy = FloatField()
    vz = FloatField()
    gs = FloatField()


class SailInfo(Model):
    # TODO: Pass version from the parent model
    orbit = UInt32Field()
    node = UInt32Field()
    kill = UInt32Field()
    posr_x = FloatField()
    posr_y = FloatField()
    posr_z = FloatField()


class ExpiryOrder(Model):
    time = Int64Field()
    index = Int32Field()


class AbsorbOrder(Model):
    time = Int64Field()
    index = Int32Field()
    layer = Int32Field()
    node = Int32Field()


class DysonSwarm(Model):
    version = Int32Field()
    versionCheck1 = ConditionalBlockStart(arg_fields='version', condition_func=ge(1))
    randSeed = Int32Field()
    sailCapacity = Int32Field()
    sailCursor = Int32Field()
    sailRecycleCursor = Int32Field()
    sailPoolForSave = ArrayField(lambda: ModelField(Sail), length_field='sailCursor')
    sailInfos = ArrayField(lambda: ModelField(SailInfo), length_field='sailCursor')
    sailRecycle = ArrayField(Int32Field, length_field='sailRecycleCursor')
    orbitCapacity = Int32Field()
    orbitCursor = Int32Field()
    orbits = ArrayField(lambda: ModelField(SailOrbit), length_field='orbitCursor', length_func=decr())
    numExpiryOrder = Int32Field()
    expiryCursor = Int32Field()
    expiryEnding = Int32Field()
    expiryOrder = ArrayField(lambda: ModelField(ExpiryOrder), length_field='numExpiryOrder')
    versionCheck2 = ConditionalBlockStart(arg_fields='version', condition_func=ge(2))
    numAbsorbOrder = Int32Field()
    absorbCursor = Int32Field()
    absorbEnding = Int32Field()
    absorbOrder = ArrayField(lambda: ModelField(AbsorbOrder), length_field='numAbsorbOrder')
    versionCheck3 = ConditionalBlockStart(arg_fields='version', condition_func=ge(1))
    bulletCapacity = Int32Field()
    bulletCursor = Int32Field()
    bulletRecycleCursor = Int32Field()
    bulletPool = ArrayField(lambda: ModelField(SailBullet), length_field='bulletCursor', length_func=decr())
    bulletRecycle = ArrayField(Int32Field, length_field='bulletRecycleCursor')
