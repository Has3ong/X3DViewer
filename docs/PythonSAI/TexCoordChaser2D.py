from . import *

# TexCoordChaser2D defines a concrete node interface that extends interface X3DChaserNode.
class CTexCoordChaser2D(CX3DChaserNode):
    m_strNodeName = "TexCoordChaser2D"
    def __init__(self):
        self.m_strNodeName = "TexCoordChaser2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign 2-tuple float array [] to MFVec2f inputOnly field named "set_destination"
    def setDestination (self, values):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOnly field named "set_value"
    def setValue (self, values):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return number of 2-tuple primitive values in "value_changed" array
    def getNumValue (self):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f initializeOnly field named "initialDestination"
    def getInitialDestination (self):
        pass

    # Return number of 2-tuple primitive values in "initialDestination" array
    def getNumInitialDestination (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f initializeOnly field named "initialDestination"
    def setInitialDestination (self, values):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f initializeOnly field named "initialValue"
    def getInitialValue (self):
        pass

    # Return number of 2-tuple primitive values in "initialValue" array
    def getNumInitialValue (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f initializeOnly field named "initialValue"
    def setInitialValue (self, values):
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
