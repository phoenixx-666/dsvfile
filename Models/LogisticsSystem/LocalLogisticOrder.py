from Fields import Int32Field
from Models import Model


"""
LocalLogisticOrder
{
    int32 version = 0
    int32 otherStationId
    int32 thisIndex
    int32 otherIndex
    int32 itemId
    int32 thisOrdered
    int32 otherOrdered
}
"""


class LocalLogisticOrder(Model):
    version = Int32Field()
    otherStationId = Int32Field()
    thisIndex = Int32Field()
    otherIndex = Int32Field()
    itemId = Int32Field()
    thisOrdered = Int32Field()
    otherOrdered = Int32Field()
