from Field import UInt8Field, Int16Field, Int32Field, FloatField, ArrayField
from Reader import Reader


"""
PrebuildData
{
    uint8 version = 0
    int32 id
    int16 protoId
    int16 modelIndex
    float pos_x
    float pos_y
    float pos_z
    float rot_x
    float rot_y
    float rot_z
    float rot_w
    float pos2_x
    float pos2_y
    float pos2_z
    float rot2_x
    float rot2_y
    float rot2_z
    float rot2_w
    int32 upEntity
    int16 pickOffset
    int16 insertOffset
    int32 recipeId
    int32 filterId
    int32 refCount
    int32 refArr[refCount]
}
"""


class PrebuildData(Reader):
    version = UInt8Field()
    id = Int32Field()
    protoId = Int16Field()
    modelIndex = Int16Field()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    rot_x = FloatField()
    rot_y = FloatField()
    rot_z = FloatField()
    rot_w = FloatField()
    pos2_x = FloatField()
    pos2_y = FloatField()
    pos2_z = FloatField()
    rot2_x = FloatField()
    rot2_y = FloatField()
    rot2_z = FloatField()
    rot2_w = FloatField()
    upEntity = Int32Field()
    pickOffset = Int16Field()
    insertOffset = Int16Field()
    recipeId = Int32Field()
    filterId = Int32Field()
    refArr = ArrayField(Int32Field)
