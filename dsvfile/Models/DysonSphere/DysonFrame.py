from ...Fields import BoolField
from . import Model, Int32Field


class DysonFrame(Model):
    version = Int32Field()
    id = Int32Field()
    protoId = Int32Field()
    layerId = Int32Field()
    reserved = BoolField()
    nodeId = Int32Field()
    nodeId2 = Int32Field()
    euler = BoolField()
    spA = Int32Field()
    spB = Int32Field()
    spMax = Int32Field()
