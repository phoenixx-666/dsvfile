from ...Fields import FloatField, BoolField
from ...Func import ge
from . import Model, Int32Field, ConditionalField


"""
DysonNode
{
    int32 version = 4
    int32 id
    int32 protoId
    int32 layerId
    uint8_bool use
    uint8_bool reserved
    float pos_x
    float pos_y
    float pos_z
    int32 sp
    int32 spMax
    int32 spOrdered
    int32 cpOrdered (version >= 3)
    int32 rid (version >= 2)
    int32 frameTurn
    int32 shellTurn (version >= 1)
    int32 _spReq
    int32 _cpReq (version >= 4)
}
"""


class DysonNode(Model):
    version = Int32Field()
    id = Int32Field()
    protoId = Int32Field()
    layerId = Int32Field()
    use = BoolField()
    reserved = BoolField()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    sp = Int32Field()
    spMax = Int32Field()
    spOrdered = Int32Field()
    cpOrdered = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(3))
    rid = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(2))
    frameTurn = Int32Field()
    shellTurn = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(1))
    spReq = Int32Field()
    cpReq = ConditionalField(Int32Field, arg_fields='version', condition_func=ge(4))
