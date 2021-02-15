from Field import Int32Field,  Int64Field, FloatField, ByteStringField, ReaderField, ArrayField
from Field.Enums import EVeinType
from Reader import Reader


"""
PlanetData
{
    int32 modDataByteCount
    uint8 modData[modDataByteCount]
    int32 numVeinAmounts
    int64 veinAmounts[numVeinAmounts]: The index is the EVeinType.  This contains the total of the veinGroups's amounts which is also the total of the VeinData::amounts.
    int32 numVeinGroups
    veinGroups[numVeinGroups] {
        int32 EVeinType type (None, Iron, Copper, Silicium, Titanium, Stone, Coal, Oil, Fireice, Diamond, Fractal, Crysrub, Grat, Bamboo, Mag)
        float pos_x
        float pos_y
        float pos_z
        int32 count: Read, but then set to zero
        int64 amount: Read, but then set to zero
    }
}
"""


class VeinGroup(Reader):
    veinType = EVeinType()
    pos_x = FloatField()
    pos_y = FloatField()
    pos_z = FloatField()
    count = Int32Field()
    amount = Int64Field()


class PlanetData(Reader):
    modData = ByteStringField()
    veinAmounts = ArrayField(Int64Field)
    veinGroups = ArrayField(lambda: ReaderField(VeinGroup))
