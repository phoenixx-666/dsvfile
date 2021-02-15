from Field import Int32Field, ReaderField, ArrayField
from Reader import Reader
from Readers.FactoryProductionStat import FactoryProductionStat


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


class ProductionStatistics(Reader):
    version = Int32Field()
    factoryStatPool = ArrayField(lambda: ReaderField(FactoryProductionStat))
    firstCreateIds = ArrayField(Int32Field)
    favoriteIds = ArrayField(Int32Field)
