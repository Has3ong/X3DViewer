from . import *

# ForcePhysicsModel defines a concrete node interface that extends interface X3DParticlePhysicsModelNode.
class CForcePhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "ForcePhysicsModel"
    def __init__(self):
        self.m_strNodeName = "ForcePhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "force"
    def getForce (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "force"
    def setForce (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

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
