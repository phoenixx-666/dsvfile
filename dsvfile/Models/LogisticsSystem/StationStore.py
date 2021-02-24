from ...Fields.Enums import ELogisticStorage
from . import Model, Int32Field


class StationStore(Model):
    version = Int32Field()
    itemId = Int32Field()
    count = Int32Field()
    localOrder = Int32Field()
    remoteOrder = Int32Field()
    max = Int32Field()
    localLogic = ELogisticStorage()
    remoteLogic = ELogisticStorage()
