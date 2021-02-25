from ...Fields import BoolField, ConditionalBlockStart
from ...Fields.Enums import ERecipe, ERecipeType
from ...Func import g
from . import Model, Int32Field, ArrayField


class AssemblerComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    replicating = BoolField()
    outputing = BoolField()
    speed = Int32Field()
    time = Int32Field()
    recipeId = ERecipe()
    recipeIdChecker = ConditionalBlockStart(arg_fields='recipeId', condition_func=g(0))
    recipeType = ERecipeType()
    timeSpend = Int32Field()
    requires = ArrayField(Int32Field)
    requireCounts = ArrayField(Int32Field)
    served = ArrayField(Int32Field)
    needs = ArrayField(Int32Field)
    products = ArrayField(Int32Field)
    productCounts = ArrayField(Int32Field)
    produced = ArrayField(Int32Field)
