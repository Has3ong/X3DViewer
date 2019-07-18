from . import *

# X3DPointingDeviceSensorNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
class CX3DPointingDeviceSensorNode(CX3DSensorNode):
    m_strNodeName = "CX3DPointingDeviceSensorNode"
    def __init__(self):
        self.m_strNodeName = "X3DPointingDeviceSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return bool result from SFBool outputOnly field named "isOver"
    def getIsOver (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
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
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass