from . import *

# WorldInfo defines a concrete node interface that extends interface X3DInfoNode
class CWorldInfo(CX3DInfoNode):
    m_strNodeName = "WorldInfo"
    def __init__(self):
        self.m_strNodeName = "WorldInfo"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array [] from MFString initializeOnly field named "info"
    def getInfo (self):
        pass

    # Return number of primitive values in "info" array
    def getNumInfo (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "info"
    def setInfo1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "info"
    def setInfo2 (self, value):
        pass

    # Return String result [] from SFString initializeOnly field named "title"
    def getTitle (self):
        pass

    # Assign String value [] to SFString initializeOnly field named "title"
    def setTitle (self, value):
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
