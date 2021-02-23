from Fields import UInt8Field, Int16Field, Int32Field, FloatField
from Models import Model

"""
EntityData
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
    int32 beltId
    int32 splitterId
    int32 storageId
    int32 tankId
    int32 minerId
    int32 inserterId
    int32 assemblerId
    int32 fractionateId
    int32 ejectorId
    int32 siloId
    int32 labId
    int32 stationId
    int32 powerNodeId
    int32 powerGenId
    int32 powerConId
    int32 powerAccId
    int32 powerExcId
    int32 monsterId
}
"""


class EntityData(Model):
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
    beltId = Int32Field()
    splitterId = Int32Field()
    storageId = Int32Field()
    tankId = Int32Field()
    minerId = Int32Field()
    inserterId = Int32Field()
    assemblerId = Int32Field()
    fractionateId = Int32Field()
    ejectorId = Int32Field()
    siloId = Int32Field()
    labId = Int32Field()
    stationId = Int32Field()
    powerNodeId = Int32Field()
    powerGenId = Int32Field()
    powerConId = Int32Field()
    powerAccId = Int32Field()
    powerExcId = Int32Field()
    monsterId = Int32Field()
