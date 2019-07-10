from . import *

# SplinePositionInterpolator2D defines a concrete node interface that extends interface X3DInterpolatorNode.
class CSplinePosiionInterpolator2D(CX3DInterpolatorNode):
    m_strNodeName = "SplinePosiionInterpolator2D"
    def __init__(self):
        self.m_strNodeName = "SplinePosiionInterpolator2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 2-tuple float results array [] from SFVec2f outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return boolean result from SFBool initializeOnly field named "closed"
    def getClosed (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "closed"
    def setClosed (self, value):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f inputOutput field named "keyValue"
    def getKeyValue (self):
        pass

    # Return number of 2-tuple primitive values in "keyValue" array
    def getNumKeyValue (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOutput field named "keyValue"
    def setKeyValue (self, values, size):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f inputOutput field named "keyVelocity"
    def getKeyVelocity (self, result):
        pass

    # Return number of 2-tuple primitive values in "keyVelocity" array
    def getNumKeyVelocity (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOutput field named "keyVelocity"
    def setKeyVelocity (self,  values):
        pass

    # Return boolean result from SFBool inputOutput field named "normalizeVelocity"
    def getNormalizeVelocity (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "normalizeVelocity"
    def setNormalizeVelocity (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Assign float value [] to SFFloat inputOnly field named "set_fraction"
    def setFraction (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "key"
    def getKey (self):
        pass

    # Return number of primitive values in "key" array
    def getNumKey (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "key"
    def setKey1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "key"
    def setKey2 (self, value):
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

    pass