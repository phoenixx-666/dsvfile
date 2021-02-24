from . import Model, Int32Field


class LocalLogisticOrder(Model):
    version = Int32Field()
    otherStationId = Int32Field()
    thisIndex = Int32Field()
    otherIndex = Int32Field()
    itemId = Int32Field()
    thisOrdered = Int32Field()
    otherOrdered = Int32Field()
