from Fields import Int32Field, ModelField, ArrayField
from Models import Model


"""
MechaForge
{
    int32 version = 0
    int32 numTasks
    ForgeTask tasks[numTasks]
}

ForgeTask
{
    int32 version = 0
    int32 recipeId
    int32 count
    int32 tick
    int32 tickSpend
    int32 numItem
    int32 numProduct
    [numItem] {
        int32 itemIds
        int32 itemCounts
        int32 served
    }
    [numProduct] {
        int32 productIds
        int32 productCounts
        int32 produced
    }
    int32 parentTaskIndex
}
"""


class Item(Model):
    itemIds = Int32Field()
    itemCounts = Int32Field()
    served = Int32Field()


class Product(Model):
    productIds = Int32Field()
    productCounts = Int32Field()
    produced = Int32Field()


class ForgeTask(Model):
    version = Int32Field()
    recipeId = Int32Field()
    count = Int32Field()
    tick = Int32Field()
    tickSpend = Int32Field()
    numItem = Int32Field()
    numProduct = Int32Field()
    items = ArrayField(lambda: ModelField(Item), length_field='numItem')
    products = ArrayField(lambda: ModelField(Item), length_field='numProduct')
    parentTaskIndex = Int32Field()


class MechaForge(Model):
    version = Int32Field()
    tasks = ArrayField(lambda: ModelField(ForgeTask))
