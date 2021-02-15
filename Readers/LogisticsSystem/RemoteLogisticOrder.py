from Field import Int32Field
from Reader import Reader


"""
RemoteLogisticOrder 
{
    int32 version = 0
    int32 otherStationGId
    int32 thisIndex
    int32 otherIndex
    int32 itemId
    int32 thisOrdered
    int32 otherOrdered
}
"""


class RemoteLogisticOrder(Reader):
    version = Int32Field()
    otherStationGId = Int32Field()
    thisIndex = Int32Field()
    otherIndex = Int32Field()
    itemId = Int32Field()
    thisOrdered = Int32Field()
    otherOrdered = Int32Field()
