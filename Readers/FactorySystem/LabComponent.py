from Field import Int32Field, BoolField, ArrayField, ConditionalBlockStart
from Func import ne
from Reader import Reader


"""
LabComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 pcId
    int32 nextLabId
    uint8_bool replicating
    uint8_bool outputing
    int32 time
    int32 hashBytes
    uint8_bool researchMode
    int32 recipeId
    int32 techId
    (not researchMode and recipeId > 0) {
        int32 timeSpend
        int32 numRequires
        int32 requires[numRequires]
        int32 numRequireCounts
        int32 requireCounts[numRequireCounts]
        int32 numServed
        int32 served[numServed]
        int32 numNeeds
        int32 needs[numNeeds]
        int32 numProducts
        int32 products[numProducts]
        int32 numProductCounts
        int32 productCounts[numProductCounts]
        int32 numProduced
        int32 produced[numProduced]
    }
    (researchMode) {
        int32 numMatrixPoints
        int32 matrixPoints[numMatrixPoints]
        int32 numMatrixServed
        int32 matrixServed[numMatrixServed]
        int32 numNeeds
        int32 needs[numNeeds]
    }
}
"""


checker_func = lambda researchMode, recipeId: researchMode == 0 and recipeId > 0


class LabComponent(Reader):
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
