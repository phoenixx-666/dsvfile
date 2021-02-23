from Fields import Int32Field, FloatField, DoubleField, BoolField, ModelField, ArrayField, ConditionalField
from Func import ge
from Models import Model
from Models import Int32KVP

"""
GamePrefsData
{
    int32 version = 2
    double cameraUPos_x
    double cameraUPos_y
    double cameraUPos_z
    float cameraURot_x
    float cameraURot_y
    float cameraURot_z
    float cameraURot_w
    int32 reformCursorSize (version >= 1)
    int32 numReplicatorMultipliers (version >= 1)
    replicatorMultipliers[numReplicatorMultipliers] (version >= 1) {
        int32 key
        int32 value
    }
    uint8_bool detailPower
    uint8_bool detailVein
    uint8_bool detailSpaceGuide
    uint8_bool detailSign
    uint8_bool detailIcon
    int32 numTutorialShowing (version >= 2)
    int32 tutorialShowing[numTutorialShowing] (version >= 2)
}
"""


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
