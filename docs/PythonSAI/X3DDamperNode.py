from . import *

# X3DDamperNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
class CX3DDamperNode(CX3DFollowerNode):
    m_strNodeName = "X3DDamperNode"
    def __init__(self):
        self.m_strNodeName = "X3DDamperNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

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

    #  ===== methods for fields inherited from parent interfaces =====

    # Return bool result from SFBool outputOnly field named "isActive"
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