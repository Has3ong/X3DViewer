from . import *

# BooleanTrigger defines a concrete node interface that extends interface X3DTriggerNode.
class CBooleanTrigger(CX3DTriggerNode):
    m_strNodeName = "BooleanTrigger"
    def __init__(self):
        self.m_strNodeName = "BooleanTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign double value in seconds to SFTime inputOnly field named "set_triggerTime"
    def setTriggerTime (self, timestamp):
        pass

    # Return boolean result from SFBool outputOnly field named "triggerTrue"
    def getTriggerTrue (self):
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