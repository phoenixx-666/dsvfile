from ...Fields import FloatField, BoolField
from ...Func import ge
from . import Model, Int32Field, ConditionalField


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
