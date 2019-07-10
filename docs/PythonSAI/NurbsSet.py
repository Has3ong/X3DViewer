from . import *

# NurbsSet defines a concrete node interface that extends interfaces X3DChildNodeX3DBoundedObject.
class CNurbsSet(CX3DChildNode):
    m_strNodeName = "NurbsSet"
    def __init__(self):
        self.m_strNodeName = "NurbsSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "tessellationScale"
    def getTessellationScale (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "tessellationScale"
    def setTessellationScale (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "bboxCenter"
    def getBboxCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "bboxCenter"
    def setBboxCenter (self, value):
        pass

    # Return array of 3-tuple float results array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 from boundingBoxSizeType type initializeOnly field named "bboxSize"
    def getBboxSize (self):
        pass

    # Assign 3-tuple float array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 to boundingBoxSizeType type initializeOnly field named "bboxSize"
    def setBboxSize (self, value):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOnly field named "addGeometry"
    def setAddGeometry1 (self, nodes):
        pass

    # Assign single X3DNurbsSurfaceGeometryNode value (using a properly typed node) as the MFNode array for inputOnly field named "addGeometry"
    def setAddGeometry2 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "addGeometry"
    def setAddGeometry3 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOnly field named "addGeometry"
    def setAddGeometry4 (self, nodes):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOnly field named "removeGeometry"
    def setRemoveGeometry1 (self, nodes):
        pass

    # Assign single X3DNurbsSurfaceGeometryNode value (using a properly typed node) as the MFNode array for inputOnly field named "removeGeometry"
    def setRemoveGeometry2 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "removeGeometry"
    def setRemoveGeometry3 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOnly field named "removeGeometry"
    def setRemoveGeometry4 (self, nodes):
        pass

    # Return array of X3DNurbsSurfaceGeometryNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "geometry"
    def getGeometry (self, result):
        pass

    # Return number of nodes in "geometry" array
    def getNumGeometry (self):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOutput field named "geometry"
    def setGeometry1 (self, nodes):
        pass

    # Assign single X3DNurbsSurfaceGeometryNode value (using a properly typed node) as the MFNode array for inputOutput field named "geometry"
    def setGeometry2 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "geometry"
    def setGeometry3 (self, node):
        pass

    # Assign X3DNurbsSurfaceGeometryNode array (using a properly typed node array) to MFNode inputOutput field named "geometry"
    def setGeometry4 (self, nodes):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
