from Fields import Int32Field, ModelField, ArrayField
from Models import Model
from Models import Int32KVP


class MechaLab(Model):
    version = Int32Field()
    itemPoints = ArrayField(lambda: ModelField(Int32KVP))
