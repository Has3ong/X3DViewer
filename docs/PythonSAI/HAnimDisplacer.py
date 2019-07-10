from . import *

# HAnimDisplacer defines a concrete node interface that extends interface X3DGeometricPropertyNode.
class CHAnimDisplacer(CX3DGeometricPropertyNode):
    m_strNodeName = "HAnimDisplacer"
    def __init__(self):
        self.m_strNodeName = "HAnimDisplacer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result from featurePointNames type inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value to featurePointNames type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "coordIndex"
    def getCoordIndex (self):
        pass

    # Return number of primitive values in "coordIndex" array
    def getNumCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "coordIndex"
    def setCoordIndex (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "coordIndex"
    def setCoordIndex (self, value):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f inputOutput field named "displacements"
    def getDisplacements (self, result):
        pass

    # Return number of 3-tuple primitive values in "displacements" array
    def getNumDisplacements (self):
        pass

    # Assign 3-tuple float array [] to MFVec3f inputOutput field named "displacements"
    def setDisplacements (self, values, size):
        pass

    # Return float result [] from SFFloat inputOutput field named "weight"
    def getWeight (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "weight"
    def setWeight (self, value):
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
