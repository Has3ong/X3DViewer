from . import *

# ViewpointGroup defines a concrete node interface that extends interface X3DChildNode.
class CViewpointGroup(CX3DViewpointNode):
    m_strNodeName = "ViewpointGroup"
    def __init__(self):
        self.m_strNodeName = "ViewpointGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "displayed"
    def getDisplayed (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "displayed"
    def setDisplayed (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "retainUserOffsets"
    def getRetainUserOffsets (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "retainUserOffsets"
    def setRetainUserOffsets (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return array of X3DViewpointNode|ViewpointGroup results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Assign X3DViewpointNode|ViewpointGroup array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "children"
    def setChildren2 (self, node):
        pass

    # Assign X3DViewpointNode|ViewpointGroup array (using a properly typed protoInstance array) to MFNode inputOutput field named "children"
    def setChildren3 (self, node):
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