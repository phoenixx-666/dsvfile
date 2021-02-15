from Field import Int32Field
from Reader import Reader


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


class LocalLogisticOrder(Reader):
    version = Int32Field()
    otherStationId = Int32Field()
    thisIndex = Int32Field()
    otherIndex = Int32Field()
    itemId = Int32Field()
    thisOrdered = Int32Field()
    otherOrdered = Int32Field()
