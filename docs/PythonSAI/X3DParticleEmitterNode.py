from . import *

# X3DParticleEmitterNode defines an abstract node interface that extends interface .
class CX3DParticleEmitterNode(CX3DNode):
    m_strNodeName = "X3DParticleEmitterNode"
    def __init__(self):
        self.m_strNodeName = "X3DParticleEmitterNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "speed"
    def getSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "speed"
    def setSpeed (self, value) :
        pass

    # Return float result [] from SFFloat inputOutput field named "variation"
    def getVariation (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "variation"
    def setVariation (self, value) :
        pass

    # Return float result [] from SFFloat inputOutput field named "mass"
    def getMass (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "mass"
    def setMass (self, value) :
        pass

    # Return float result [] from SFFloat initializeOnly field named "surfaceArea"
    def getSurfaceArea (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "surfaceArea"
    def setSurfaceArea (self, value) :
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass