from Field import Int32Field, BoolField, ArrayField, ConditionalBlockStart
from Field.Enums import ERecipeType
from Func import g
from Reader import Reader

"""
AssemblerComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 pcId
    uint8_bool replicating
    uint8_bool outputing
    int32 speed
    int32 time
    int32 recipeId
    (recipeId > 0) {
        int32 ERecipeType recipeType (0:None 1:Smelt 2:Chemical 3:Refine 4:Assemble 5:Particle 6:Exchange 7:PhotonStore 8:Fractionate 15:Research)
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
}
"""


class AssemblerComponent(Reader):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    replicating = BoolField()
    outputing = BoolField()
    speed = Int32Field()
    time = Int32Field()
    recipeId = Int32Field()
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
