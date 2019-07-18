from . import *

# X3DEnvironmentalSensorNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
class CX3DEnviromentalSensorNode(CX3DSensorNode):
    m_strNodeName = "X3DEnviromentalSensorNode"
    def __init__(self):
        self.m_strNodeName = "X3DEnviromentalSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth =0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled1 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled1 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return bool result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled2 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled2 (self, value):
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