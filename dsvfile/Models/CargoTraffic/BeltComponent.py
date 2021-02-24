from . import Model, Int32Field


class BeltComponent(Model):
    version = Int32Field()
    id = Int32Field()
    entityId = Int32Field()
    speed = Int32Field()
    segPathId = Int32Field()
    segIndex = Int32Field()
    segPivotOffset = Int32Field()
    segLength = Int32Field()
    outputId = Int32Field()
    backInputId = Int32Field()
    leftInputId = Int32Field()
    rightInputId = Int32Field()
