from ...Fields import FloatField
from ...Fields.Enums import EItem
from . import Model, Int32Field


class DroneData(Model):
    version = Int32Field()
    begin_x = FloatField()
    begin_y = FloatField()
    begin_z = FloatField()
    end_x = FloatField()
    end_y = FloatField()
    end_z = FloatField()
    endId = Int32Field()
    direction = FloatField()
    maxt = FloatField()
    t = FloatField()
    itemId = EItem()
    itemCount = Int32Field()
    gene = Int32Field()
