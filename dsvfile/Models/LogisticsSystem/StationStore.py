from ...Fields.Enums import ELogisticStorage
from . import Model, Int32Field


"""
StationStore
{
    int32 version = 0
    int32 itemId
    int32 count
    int32 localOrder
    int32 remoteOrder
    int32 max
    int32 ELogisticStorage localLogic (None, Supply, Demand)
    int32 ELogisticStorage remoteLogic
}
"""


class StationStore(Model):
    version = Int32Field()
    itemId = Int32Field()
    count = Int32Field()
    localOrder = Int32Field()
    remoteOrder = Int32Field()
    max = Int32Field()
    localLogic = ELogisticStorage()
    remoteLogic = ELogisticStorage()
