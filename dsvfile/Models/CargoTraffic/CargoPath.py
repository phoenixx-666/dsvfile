from ...Fields import FloatField, BoolField, ByteStringField
from ...Func import mul
from . import Model, Int32Field, ModelField, ArrayField


class Point(Model):
    pointPos_x = FloatField()
    pointPos_y = FloatField()
    pointPos_z = FloatField()
    pointRot_x = FloatField()
    pointRot_y = FloatField()
    pointRot_z = FloatField()
    pointRot_w = FloatField()


class CargoPath(Model):
    version = Int32Field()
    id = Int32Field()
    capacity = Int32Field()
    bufferLength = Int32Field()
    chunkCapacity = Int32Field()
    chunkCount = Int32Field()
    updateLen = Int32Field()
    closed = BoolField()
    outputPathIdForImport = Int32Field()
    outputIndex = Int32Field()
    numBelts = Int32Field()
    numInputPaths = Int32Field()
    buffer = ByteStringField(length_field='bufferLength')
    chunks = ArrayField(Int32Field, length_field='chunkCount', length_func=mul(3))
    points = ArrayField(lambda: ModelField(Point), length_field='bufferLength')
    belts = ArrayField(Int32Field, length_field='numBelts')
    inputPaths = ArrayField(Int32Field, length_field='numInputPaths')
