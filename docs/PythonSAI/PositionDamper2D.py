from . import *

# PositionDamper2D defines a concrete node interface that extends interface X3DDamperNode.
class CPositionDamper2D(CX3DDamperNode):
    m_strNodeName = "PositionDamper2D"
    def __init__(self):
        self.m_strNodeName = "PositionDamper2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign 2-tuple float array [] to SFVec2f inputOnly field named "set_destination"
    def setDestination (self, value):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOnly field named "set_value"
    def setValue (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f initializeOnly field named "initialDestination"
    def getInitialDestination (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f initializeOnly field named "initialDestination"
    def setInitialDestination (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f initializeOnly field named "initialValue"
    def getInitialValue (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f initializeOnly field named "initialValue"
    def setInitialValue (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return double result in seconds from  type inputOutput field named "tau"
    def getTau (self):
        pass

    # Assign double value in seconds to  type inputOutput field named "tau"
    def setTau (self, timestamp):
        pass

    # Return float result [] from SFFloat inputOutput field named "tolerance"
    def getTolerance (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "tolerance"
    def setTolerance (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "order"
    def getOrder (self):
        pass

    # Assign int value [] to  type initializeOnly field named "order"
    def setOrder (self, value):
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
