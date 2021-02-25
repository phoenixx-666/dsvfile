from ...Fields import UInt32Field, Int64Field, FloatField
from ...Func import ge, decr
from . import Model, Int32Field, ModelField, ArrayField, ConditionalBlockStart
from .SailOrbit import SailOrbit
from .SailBullet import SailBullet


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
    sailPoolForSave = ArrayField(ModelField(Sail), length_field='sailCursor')
    sailInfos = ArrayField(ModelField(SailInfo), length_field='sailCursor')
    sailRecycle = ArrayField(Int32Field, length_field='sailRecycleCursor')
    orbitCapacity = Int32Field()
    orbitCursor = Int32Field()
    orbits = ArrayField(ModelField(SailOrbit), length_field='orbitCursor', length_func=decr())
    numExpiryOrder = Int32Field()
    expiryCursor = Int32Field()
    expiryEnding = Int32Field()
    expiryOrder = ArrayField(ModelField(ExpiryOrder), length_field='numExpiryOrder')
    versionCheck2 = ConditionalBlockStart(arg_fields='version', condition_func=ge(2))
    numAbsorbOrder = Int32Field()
    absorbCursor = Int32Field()
    absorbEnding = Int32Field()
    absorbOrder = ArrayField(ModelField(AbsorbOrder), length_field='numAbsorbOrder')
    versionCheck3 = ConditionalBlockStart(arg_fields='version', condition_func=ge(1))
    bulletCapacity = Int32Field()
    bulletCursor = Int32Field()
    bulletRecycleCursor = Int32Field()
    bulletPool = ArrayField(ModelField(SailBullet), length_field='bulletCursor', length_func=decr())
    bulletRecycle = ArrayField(Int32Field, length_field='bulletRecycleCursor')
