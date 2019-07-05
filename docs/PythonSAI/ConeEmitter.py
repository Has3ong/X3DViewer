from . import *

# ConeEmitter defines a concrete node interface that extends interface X3DParticleEmitterNode.
class CConeEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "ConeEmitter"
    def __init__(self):
        self.m_strNodeName = "ConeEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result in radians from SFFloat inputOutput field named "angle"
    def getAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "angle"
    def setAngle (self, angle):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "direction"
    def getDirection (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "direction"
    def setDirection (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "position"
    def getPosition (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "position"
    def setPosition (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return float result [] from SFFloat inputOutput field named "speed"
    def getSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "speed"
    def setSpeed (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "variation"
    def getVariation (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "variation"
    def setVariation (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "mass"
    def getMass (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "mass"
    def setMass (self, value):
        pass

    # Return float result [] from SFFloat initializeOnly field named "surfaceArea"
    def getSurfaceArea (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "surfaceArea"
    def setSurfaceArea (self, value):
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

