from Field import Int16Field, Int32Field, FloatField, BoolField
from Field.Enums import EInserterStage
from Reader import Reader


"""
InserterComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 pcId
    int32 EInserterStage stage (Picking, Sending, Inserting, Returning)
    int32 speed
    int32 time
    int32 stt
    int32 delay
    int32 pickTarget
    int32 insertTarget
    uint8_bool careNeeds
    uint8_bool canStack
    int16 pickOffset
    int16 insertOffset
    int32 filter
    int32 itemId
    int32 stackCount
    int32 stackSize
    float pos2_x
    float pos2_y
    float pos2_z
    float rot2_x
    float rot2_y
    float rot2_z
    float rot2_w
    int16 t1
    int16 t2
}
"""


class InserterComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    stage = EInserterStage()
    speed = Int32Field()
    time = Int32Field()
    stt = Int32Field()
    delay = Int32Field()
    pickTarget = Int32Field()
    insertTarget = Int32Field()
    careNeeds = BoolField()
    canStack = BoolField()
    pickOffset = Int16Field()
    insertOffset = Int16Field()
    filter = Int32Field()
    itemId = Int32Field()
    stackCount = Int32Field()
    stackSize = Int32Field()
    pos2_x = FloatField()
    pos2_y = FloatField()
    pos2_z = FloatField()
    rot2_x = FloatField()
    rot2_y = FloatField()
    rot2_z = FloatField()
    rot2_w = FloatField()
    t1 = Int16Field()
    t2 = Int16Field()
