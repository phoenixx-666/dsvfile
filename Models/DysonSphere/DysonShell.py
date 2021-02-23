from Fields import Int32Field, FloatField, ModelField, ArrayField
from Models import Model


"""
DysonShell
{
    int32 version = 0
    int32 id
    int32 protoId
    int32 layerId
    int32 randSeed
    int32 numPolygon
    polygon[numPolygon] {
        float item_x
        float item_y
        float item_z
    }
    int32 numDysonNode
    int32 nodeId[numDysonNode]: Must be an existing ID or the game will crash.
    int32 vertexCount
    int32 triangleCount
    int32 numVerts
    verts[numVerts] {
        float x
        float y
        float z
    }
    int32 numPqArr
    pqArr[numPqArr] {
        int32 x
        int32 y
    }
    int32 numTris
    int32 tris[numTris]
    int32 numVAdjs
    int32 vAdjs[numVAdjs]
    int32 numVertAttr
    int32 vertAttr[numVertAttr]
    int32 numVertsq
    int32 vertsq[numVertsq]
    int32 numVertsqOffset
    int32 vertsqOffset[numVertsqOffset]
    int32 numNodecps
    int32 nodecps[numNodecps]
    int32 numVertcps
    int32 vertcps[numVertcps]
    int32 vertRecycleArraySize
    int32 vertRecycleCursor
    int32 vertRecycle[vertRecycleCursor]
}
"""


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
