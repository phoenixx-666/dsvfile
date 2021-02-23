from Fields import Int32Field, UInt32Field, FloatField, BoolField
from Models import Model


"""
FractionateComponent
{
    int32 version = 0
    int32 id
    int32 entityId
    int32 pcId
    int32 belt0
    int32 belt1
    int32 belt2
    uint8_bool isOutput0
    uint8_bool isOutput1
    uint8_bool isOutput2
    uint8_bool isWorking
    float produceProb
    int32 need
    int32 product
    int32 needCurrCount
    int32 productCurrCount
    int32 oriProductCurrCount
    int32 progress
    uint8_bool isRand
    uint8_bool fractionateSuccess
    int32 needMaxCount
    int32 productMaxCount
    int32 oriProductMaxCount
    uint32 seed
}
"""


class FractionateComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    pcId = Int32Field()
    belt0 = Int32Field()
    belt1 = Int32Field()
    belt2 = Int32Field()
    isOutput0 = BoolField()
    isOutput1 = BoolField()
    isOutput2 = BoolField()
    isWorking = BoolField()
    produceProb = FloatField()
    need = Int32Field()
    product = Int32Field()
    needCurrCount = Int32Field()
    productCurrCount = Int32Field()
    oriProductCurrCount = Int32Field()
    progress = Int32Field()
    isRand = BoolField()
    fractionateSuccess = BoolField()
    needMaxCount = Int32Field()
    productMaxCount = Int32Field()
    oriProductMaxCount = Int32Field()
    seed = UInt32Field()
