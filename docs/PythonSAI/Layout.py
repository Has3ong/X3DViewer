from . import *

# Layout defines a concrete node interface that extends interface X3DLayoutNode.
class CLayout(CX3DLayoutNode):
    m_strNodeName = "Layout"
    def __init__(self):
        self.m_strNodeName = "Layout"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array [] from MFString inputOutput field named "align"
    def getAlign (self):
        pass

    # Return number of primitive values in "align" array
    def getNumAlign (self):
        pass

    # Assign String array [] to MFString inputOutput field named "align"
    def setAlign1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "align"
    def setAlign2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "offset"
    def getOffset (self):
        pass

    # Return number of primitive values in "offset" array
    def getNumOffset (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "offset"
    def setOffset1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "offset"
    def setOffset2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "offsetUnits"
    def getOffsetUnits (self):
        pass

    # Return number of primitive values in "offsetUnits" array
    def getNumOffsetUnits (self):
        pass

    # Assign String array [] to MFString inputOutput field named "offsetUnits"
    def setOffsetUnits1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "offsetUnits"
    def setOffsetUnits2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "scaleMode"
    def getScaleMode (self):
        pass

    # Return number of primitive values in "scaleMode" array
    def getNumScaleMode (self):
        pass

    # Assign String array [] to MFString inputOutput field named "scaleMode"
    def setScaleMode1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "scaleMode"
    def setScaleMode2 (self, value):
        pass

    # Return array of float results array [] from MFFloat initializeOnly field named "size"
    def getSize (self):
        pass

    # Return number of primitive values in "size" array
    def getNumSize (self):
        pass

    # Assign float array [] to MFFloat initializeOnly field named "size"
    def setSize1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for initializeOnly field named "size"
    def setSize2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "sizeUnits"
    def getSizeUnits (self):
        pass

    # Return number of primitive values in "sizeUnits" array
    def getNumSizeUnits (self):
        pass

    # Assign String array [] to MFString inputOutput field named "sizeUnits"
    def setSizeUnits1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "sizeUnits"
    def setSizeUnits2 (self, value):
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