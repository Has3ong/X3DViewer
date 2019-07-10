from . import *

# SurfaceEmitter defines a concrete node interface that extends interface X3DParticleEmitterNode.
class CSurfaceEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "SurfaceEmitter"
    def __init__(self):
        self.m_strNodeName = "SurfaceEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign MFInt32 value [] to MFInt32 inputOnly field named "set_coordIndex"
    def setCoordIndex (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOnly field named "set_coordIndex"
    def setCoordIndex2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 initializeOnly field named "coordIndex"
    def getCoordIndex (self):
        pass

    # Return number of primitive values in "coordIndex" array
    def getNumCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 initializeOnly field named "coordIndex"
    def setCoordIndex3 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for initializeOnly field named "coordIndex"
    def setCoordIndex4 (self, value):
        pass

    # Return X3DGeometryNode result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "surface"
    def getSurface (self, result):
        pass

    # Assign X3DGeometryNode value (using a properly typed node) to SFNode initializeOnly field named "surface"
    def setSurface (self, node):
        pass

    # Assign X3DGeometryNode value (using a properly typed protoInstance)
    def setSurface (self, protoInstance):
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
