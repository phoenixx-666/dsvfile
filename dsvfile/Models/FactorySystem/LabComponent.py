from ...Fields import BoolField, ConditionalBlockStart
from ...Func import ne
from . import Model, Int32Field, ArrayField


checker_func = lambda researchMode, recipeId: researchMode == 0 and recipeId > 0


class LabComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    nextLabId = Int32Field()
    replicating = BoolField()
    outputing = BoolField()
    time = Int32Field()
    hashBytes = Int32Field()
    researchMode = BoolField()
    recipeId = Int32Field()
    techId = Int32Field()
    researchRecipeCheck = ConditionalBlockStart(
        arg_fields=['researchMode', 'recipeId'], condition_func=checker_func)
    timeSpend = Int32Field()
    requires = ArrayField(Int32Field)
    requireCounts = ArrayField(Int32Field)
    served = ArrayField(Int32Field)
    needs = ArrayField(Int32Field)
    products = ArrayField(Int32Field)
    productCounts = ArrayField(Int32Field)
    produced = ArrayField(Int32Field)
    researchModeCheck = ConditionalBlockStart(arg_fields='researchMode', condition_func=ne(0))
    matrixPoints = ArrayField(Int32Field)
    matrixServed = ArrayField(Int32Field)
    needs2 = ArrayField(Int32Field)
