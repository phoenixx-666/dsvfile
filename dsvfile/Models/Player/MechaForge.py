from ...Fields import ArrayField
from ...Fields.Enums import EItem, ERecipe
from . import Model, Int32Field, ModelField


class Item(Model):
    itemIds = EItem()
    itemCounts = Int32Field()
    served = Int32Field()


class Product(Model):
    productIds = Int32Field()
    productCounts = Int32Field()
    produced = Int32Field()


class ForgeTask(Model):
    version = Int32Field()
    recipeId = ERecipe()
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
