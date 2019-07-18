from . import *

# X3DBindableNode defines an abstract node interface that extends interfaces X3DNode.
# Bindable nodes implement the binding stack, so that only one of each node type is active at a given time.
class CX3DBindableNode(CX3DChildNode):
    m_strNodeName = "X3DBindanbleNode"
    bound = True
    bindTime = 0.0
    def __init__(self):
        self.m_strNodeName = "X3DBindableNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.bound = True
        self.bindTime = 0.0

    # Assign bool value to SFBool inputOnly field named "set_bind"
    def setBind(self, value):
        self.bound = value

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime(self):
        return self.bindTime

    # Return bool result from SFBool outputOnly field named "isBound"
    def getIsBound(self):
        return self.bound

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