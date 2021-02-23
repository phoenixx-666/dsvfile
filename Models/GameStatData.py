from Fields import Int32Field, ModelField, ArrayField
from Models import Model
from Models.ProductionStatistics import ProductionStatistics


"""
GameStatData
{
    int32 version = 0
    int32 numTechHashedHistory
    int32 techHashedHistory[numTechHashedHistory]
    ProductionStatistics
}
"""


class GameStatData(Model):
    version = Int32Field()
    techHashedHistory = ArrayField(Int32Field)
    productionStatistics = ModelField(ProductionStatistics)
