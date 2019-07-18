from . import *

#  X3DDragSensorNode defines an abstract node interface that extends interfaces X3DSensorNode, X3DChildNode, X3DNode.
class CX3DDragSensorNode(CX3DPointingDeviceSensorNode):
    m_strNodeName = "X3DDragSensorNode"
    def __init__(self):
        self.m_strNodeName = "X3DDragSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "trackPoint_changed"
    def getTrackPoint (self):
        pass

    # Return bool result from SFBool inputOutput field named "autoOffset"
    def getAutoOffset (self):
        pass

    # Assign bool value to SFBool inputOutput field named "autoOffset"
    def setAutoOffset (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription1 (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription1 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return bool result from SFBool outputOnly field named "isOver"
    def getIsOver (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription2 (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription2 (self, value):
        pass

    # Return bool result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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
