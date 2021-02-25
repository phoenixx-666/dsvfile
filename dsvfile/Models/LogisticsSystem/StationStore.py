from ...Fields.Enums import EItem, ELogisticStorage
from . import Model, Int32Field


class StationStore(Model):
    version = Int32Field()
    itemId = EItem()
    count = Int32Field()
    localOrder = Int32Field()
    remoteOrder = Int32Field()
    max = Int32Field()
    localLogic = ELogisticStorage()
    remoteLogic = ELogisticStorage()
