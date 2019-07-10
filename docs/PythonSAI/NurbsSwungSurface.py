from . import *

# NurbsSwungSurface defines a concrete node interface that extends interface X3DParametricGeometryNode.
class CNurbsSwungSurface(CX3DParametricGeometryNode):
    m_strNodeName = "NurbsSwungSurface"
    def __init__(self):
        self.m_strNodeName = "NurbsSwungSurface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool initializeOnly field named "ccw"
    def getCcw (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "ccw"
    def setCcw (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
        pass

    # Return X3DNurbsControlCurveNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "profileCurve"
    def getProfileCurve (self, result):
        pass

    # Assign X3DNurbsControlCurveNode value (using a properly typed node) to SFNode inputOutput field named "profileCurve"
    def setProfileCurve1 (self, node):
        pass

    # Assign X3DNurbsControlCurveNode value (using a properly typed protoInstance)
    def setProfileCurve2 (self, protoInstance):
        pass

    # Return X3DNurbsControlCurveNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "trajectoryCurve"
    def getTrajectoryCurve (self, result):
        pass

    # Assign X3DNurbsControlCurveNode value (using a properly typed node) to SFNode inputOutput field named "trajectoryCurve"
    def setTrajectoryCurve1 (self, node):
        pass

    # Assign X3DNurbsControlCurveNode value (using a properly typed protoInstance)
    def setTrajectoryCurve2 (self, protoInstance):
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
