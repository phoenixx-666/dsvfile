from ..Fields import ModelField, ArrayField
from . import Model, Int32Field
from .ProductionStatistics import ProductionStatistics


class GameStatData(Model):
    version = Int32Field()
    techHashedHistory = ArrayField(Int32Field)
    productionStatistics = ModelField(ProductionStatistics)
