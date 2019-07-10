from . import *

# IntegerTrigger defines a concrete node interface that extends interface X3DTriggerNode.
class CIntegerTrigger(CX3DTriggerNode):
    m_strNodeName = "IntegerTrigger"
    def __init__(self):
        self.m_strNodeName = "IntegerTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign boolean value to SFBool inputOnly field named "set_boolean"
    def setBoolean (self, value):
        pass

    # Return int result [] from SFInt32 outputOnly field named "triggerValue"
    def getTriggerValue (self):
        pass

    # Return int result [] from SFInt32 inputOutput field named "integerKey"
    def getIntegerKey (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "integerKey"
    def setIntegerKey (self, value):
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
