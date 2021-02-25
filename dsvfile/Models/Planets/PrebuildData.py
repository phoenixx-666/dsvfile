from ...Fields import UInt8Field, Int16Field
from ...Fields.Enums import ERecipe
from . import Model, Int32Field, FloatField, ArrayField


class PrebuildData(Model):
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
    recipeId = ERecipe()
    filterId = Int32Field()
    refArr = ArrayField(Int32Field)
