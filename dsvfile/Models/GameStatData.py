from ..Fields import ModelField, ArrayField
from . import Model, Int32Field
from .ProductionStatistics import ProductionStatistics


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
