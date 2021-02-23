from Fields import Int32Field, ModelField, ArrayField
from Models import Model
from Models.FactoryProductionStat import FactoryProductionStat


"""
ProductionStatistics
{
    int32 version = 0
    int32 numFactoryStatPool
    FactoryProductionStat factoryStatPool[numFactoryStatPool]
    int32 numFirstCreateIds
    int32 firstCreateIds[numFirstCreateIds]
    int32 numFavoriteIds
    int32 favoriteIds[numFavoriteIds]
}
"""


class ProductionStatistics(Model):
    version = Int32Field()
    factoryStatPool = ArrayField(lambda: ModelField(FactoryProductionStat))
    firstCreateIds = ArrayField(Int32Field)
    favoriteIds = ArrayField(Int32Field)