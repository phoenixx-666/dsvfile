from ..Fields import FloatField, DoubleField, BoolField, ModelField, ArrayField, ConditionalField
from ..Func import ge
from . import Model, Int32KVP, Int32Field


class GamePrefsData(Model):
    version = Int32Field()
    cameraUPos_x = DoubleField()
    cameraUPos_y = DoubleField()
    cameraUPos_z = DoubleField()
    cameraURot_x = FloatField()
    cameraURot_y = FloatField()
    cameraURot_z = FloatField()
    cameraURot_w = FloatField()
    reformCursorSize = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(1))
    replicatorMultipliers = ConditionalField(lambda: ArrayField(lambda: ModelField(Int32KVP)),
                                             arg_fields='version', condition_func=ge(1))
    detailPower = BoolField()
    detailVein = BoolField()
    detailSpaceGuide = BoolField()
    detailSign = BoolField()
    detailIcon = BoolField()
    tutorialShowing = ConditionalField(lambda: ArrayField(Int32Field), arg_fields='version', condition_func=ge(2))
