from . import *

# StringSensor defines a concrete node interface that extends interface X3DKeyDeviceSensorNode.
class CStringSensor(CX3DKeyDeviceSensorNode):
    m_strNodeName = "StringSensor"
    def __init__(self):
        self.m_strNodeName = "StringSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from SFString outputOnly field named "enteredText"
    def getEnteredText (self):
        pass

    # Return String result [] from SFString outputOnly field named "finalText"
    def getFinalText (self):
        pass

    # Return boolean result from SFBool inputOutput field named "deletionAllowed"
    def getDeletionAllowed (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "deletionAllowed"
    def setDeletionAllowed (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
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
