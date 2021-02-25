from ..Fields import ModelField, ArrayField
from . import Model, Int32Field
from .FactoryProductionStat import FactoryProductionStat


class ProductionStatistics(Model):
    version = Int32Field()
    factoryStatPool = ArrayField(ModelField(FactoryProductionStat))
    firstCreateIds = ArrayField(Int32Field)
    favoriteIds = ArrayField(Int32Field)
