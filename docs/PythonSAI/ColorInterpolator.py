from . import *

# ColorInterpolator defines a concrete node interface that extends interface X3DInterpolatorNode.
class CColorInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "ColorInterpolator"
    def __init__(self):
        self.m_strNodeName = "ColorInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "keyValue"
    def getKeyValue (self):
        pass

    # Return number of 3-tuple primitive values in "keyValue" array
    def getNumKeyValue (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "keyValue"
    def setKeyValue (self, values, size):
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
