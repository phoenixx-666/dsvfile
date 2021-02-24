from ...Fields import BoolField
from . import Model, Int32Field


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
