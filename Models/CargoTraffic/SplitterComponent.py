from Fields import Int32Field, BoolField
from Models import Model


"""
SplitterComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 beltA
    int32 beltB
    int32 beltC
    int32 beltD
    int32 input0
    int32 input1
    int32 input2
    int32 input3
    int32 output0
    int32 output1
    int32 output2
    int32 output3
    uint8_bool inPriority
    uint8_bool outPriority
    int32 outFilter
}
"""


class SplitterComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    beltA = Int32Field()
    beltB = Int32Field()
    beltC = Int32Field()
    beltD = Int32Field()
    input0 = Int32Field()
    input1 = Int32Field()
    input2 = Int32Field()
    input3 = Int32Field()
    output0 = Int32Field()
    output1 = Int32Field()
    output2 = Int32Field()
    output3 = Int32Field()
    inPriority = BoolField()
    outPriority = BoolField()
    outFilter = Int32Field()
