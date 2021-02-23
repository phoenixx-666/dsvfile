from Fields import Int32Field
from Models import Model


"""
BeltComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 speed
    int32 segPathId
    int32 segIndex
    int32 segPivotOffset
    int32 segLength
    int32 outputId
    int32 backInputId
    int32 leftInputId
    int32 rightInputId
}
"""


class BeltComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    speed = Int32Field()
    segPathId = Int32Field()
    segIndex = Int32Field()
    segPivotOffset = Int32Field()
    segLength = Int32Field()
    outputId = Int32Field()
    backInputId = Int32Field()
    leftInputId = Int32Field()
    rightInputId = Int32Field()
