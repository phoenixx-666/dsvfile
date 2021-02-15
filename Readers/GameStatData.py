from Field import Int32Field, ReaderField, ArrayField
from Reader import Reader
from Readers.ProductionStatistics import ProductionStatistics


"""
GameStatData
{
    int32 version = 0
    int32 numTechHashedHistory
    int32 techHashedHistory[numTechHashedHistory]
    ProductionStatistics
}
"""


class GameStatData(Reader):
    version = Int32Field()
    techHashedHistory = ArrayField(Int32Field)
    productionStatistics = ReaderField(ProductionStatistics)
