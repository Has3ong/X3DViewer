from . import *

# WindPhysicsModel defines a concrete node interface that extends interface X3DParticlePhysicsModelNode.
class CWindPhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "WindPhysicsModel"
    def __init__(self):
        self.m_strNodeName = "WindPhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "direction"
    def getDirection (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "direction"
    def setDirection (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "gustiness"
    def getGustiness (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "gustiness"
    def setGustiness (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "speed"
    def getSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "speed"
    def setSpeed (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "turbulence"
    def getTurbulence (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "turbulence"
    def setTurbulence (self, value):
        pass

    #  ===== methods for fields inherited from parent interfaces =====

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
