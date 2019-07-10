from . import *

# TimeTrigger defines a concrete node interface that extends interface X3DTriggerNode.
class CTimeTrigger(CX3DTriggerNode):
    m_strNodeName = "TimeTrigger"
    def __init__(self):
        self.m_strNodeName = "TimeTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign boolean value to SFBool inputOnly field named "set_boolean"
    def setBoolean (self, value):
        pass

    # Return int result [] from SFInt32 outputOnly field named "triggerTime"
    def getTriggerTime (self):
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
