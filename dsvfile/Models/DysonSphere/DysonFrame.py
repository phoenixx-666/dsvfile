from ...Fields import BoolField
from . import Model, Int32Field


"""
DysonFrame
{
    int32 version = 0
    int32 id
    int32 protoId
    int32 layerId
    uint8_bool reserved
    int32 nodeId
    int32 nodeId2
    uint8_bool euler
    int32 spA
    int32 spB
    int32 spMax
}
"""


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
