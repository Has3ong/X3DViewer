from . import *

# PositionChaser defines a concrete node interface that extends interface X3DChaserNode.
class CPositionChaser(CX3DChaserNode):
    m_strNodeName = "PositionChaser"
    def __init__(self):
        self.m_strNodeName = "PositionChaser"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign 3-tuple float array [] to SFVec3f inputOnly field named "set_destination"
    def setDestination (self, value):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOnly field named "set_value"
    def setValue (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "initialDestination"
    def getInitialDestination (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "initialDestination"
    def setInitialDestination (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "initialValue"
    def getInitialValue (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "initialValue"
    def setInitialValue (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return double result in seconds from  type initializeOnly field named "duration"
    def getDuration (self):
        pass

    # Assign double value in seconds to  type initializeOnly field named "duration"
    def setDuration (self, timestamp):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
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
    #