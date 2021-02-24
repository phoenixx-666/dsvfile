from ...Fields import FloatField
from . import Model, Int32Field, ModelField, ArrayField


class Point(Model):
    x = Int32Field()
    y = Int32Field()


class Polygon(Model):
    item_x = FloatField()
    item_y = FloatField()
    item_z = FloatField()


class Vert(Model):
    x = FloatField()
    y = FloatField()
    z = FloatField()


class DysonShell(Model):
    version = Int32Field()
    id = Int32Field()
    protoId = Int32Field()
    layerId = Int32Field()
    randSeed = Int32Field()
    polygon = ArrayField(lambda: ModelField(Polygon))
    nodeId = ArrayField(Int32Field)
    vertexCount = Int32Field()
    triangleCount = Int32Field()
    verts = ArrayField(lambda: ModelField(Vert))
    pqArr = ArrayField(lambda: ModelField(Point))
    tris = ArrayField(Int32Field)
    vAdjs = ArrayField(Int32Field)
    vertAttr = ArrayField(Int32Field)
    vertsq = ArrayField(Int32Field)
    vertsqOffset = ArrayField(Int32Field)
    nodecps = ArrayField(Int32Field)
    vertcps = ArrayField(Int32Field)
    vertRecycleArraySize = Int32Field()
    vertRecycle = ArrayField(Int32Field)
