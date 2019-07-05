from . import *

# ContourPolyline2D defines a concrete node interface that extends interface X3DNurbsControlCurveNode.
class CContourPolyline2D(CX3DNurbsControlCurveNode):
    m_strNodeName = "ContourPolyline2D"
    def __init__(self):
        self.m_strNodeName = "ContourPolyline2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 2-tuple double results array [] from MFVec2d inputOutput field named "controlPoint"
    def getControlPoint (self):
        pass

    # Return number of 2-tuple primitive values in "controlPoint" array
    def getNumControlPoint (self):
        pass

    # Assign 2-tuple double array [] to MFVec2d inputOutput field named "controlPoint"
    def setControlPoint (self, values, size):
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
