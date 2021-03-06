from . import *

# ArcClose2D defines a concrete node interface that extends interface X3DGeometryNode.
class CArcClose2D(CX3DGeometryNode):
    m_strNodeName = "ArcClose2D"

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from  type initializeOnly field named "radius"
    def getRadius (self):
        pass

    # Assign float value [] to  type initializeOnly field named "radius"
    def setRadius (self, value):
        pass

    # Return float result in radians from  type initializeOnly field named "startAngle"
    def getStartAngle (self):
        pass

    # Assign float value in radians to  type initializeOnly field named "startAngle"
    def setStartAngle (self, angle):
        pass

    # Return float result in radians from  type initializeOnly field named "endAngle"
    def getEndAngle (self):
        pass

    # Assign float value in radians to  type initializeOnly field named "endAngle"
    def setEndAngle (self, angle):
        pass

    # Return String enumeration result ("PIE"|"CHORD") from ArcClose2dTypeValues type initializeOnly field named "closureType"
    def getClosureType (self):
        pass

    # Assign String enumeration value ("PIE"|"CHORD") to ArcClose2dTypeValues type initializeOnly field named "closureType"
    def setClosureType (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
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
