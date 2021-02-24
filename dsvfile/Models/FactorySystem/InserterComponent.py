from ...Fields import Int16Field, FloatField, BoolField
from ...Fields.Enums import EInserterStage
from . import Model, Int32Field


class InserterComponent(Model):
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
