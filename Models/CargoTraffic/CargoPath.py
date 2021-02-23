from Fields import Int32Field, FloatField, BoolField, ByteStringField, ModelField, ArrayField
from Func import mul
from Models import Model


"""
CargoPath
{
    int32 version = 0
    int32 id
    int32 capacity
    int32 bufferLength
    int32 chunkCapacity
    int32 chunkCount
    int32 updateLen
    uint8_bool closed
    int32 outputPathIdForImport
    int32 outputIndex
    int32 numBelts
    int32 numInputPaths
    uint8 buffer[bufferLength]
    int32 chunks[chunkCount * 3]
    [bufferLength] {
        float pointPos_x
        float pointPos_y
        float pointPos_z
        float pointRot_x
        float pointRot_y
        float pointRot_z
        float pointRot_w
    }
    int32 belts[numBelts]
    int32 inputPaths[numInputPaths]
}
"""


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
