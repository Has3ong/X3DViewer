from . import *

# Disk2D defines a concrete node interface that extends interface X3DGeometryNode.
class CDisc2D(CX3DGeometryNode):
    m_strNodeName = "Disk2D"
    def __init__(self):
        self.m_strNodeName = "Disk2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return float result [] from  type initializeOnly field named "innerRadius"
    def getInnerRadius (self):
        pass

    # Assign float value [] to  type initializeOnly field named "innerRadius"
    def setInnerRadius (self, value):
        pass

    # Return float result [] from  type initializeOnly field named "outerRadius"
    def getOuterRadius (self):
        pass

    # Assign float value [] to  type initializeOnly field named "outerRadius"
    def setOuterRadius (self, value):
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
