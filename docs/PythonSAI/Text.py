from . import *

# Text defines a concrete node interface that extends interface X3DGeometryNode.
class CText(CX3DGeometryNode):
    m_strNodeName = "Text"
    def __init__(self):
        self.m_strNodeName = "Text"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 2-tuple float results array [] from MFVec2f outputOnly field named "lineBounds"
    def getLineBounds (self):
        pass

    # Return number of 2-tuple primitive values in "lineBounds" array
    def getNumLineBounds (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "origin"
    def getOrigin (self):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f outputOnly field named "textBounds"
    def getTextBounds (self):
        pass

    # Return array of String results array [] from MFString inputOutput field named "string"
    def getString (self):
        pass

    # Return number of primitive values in "string" array
    def getNumString (self):
        pass

    # Assign String array [] to MFString inputOutput field named "string"
    def setString1 (self, values,):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "string"
    def setString2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "length"
    def getLength (self):
        pass

    # Return number of primitive values in "length" array
    def getNumLength (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "length"
    def setLength1 (self, values):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "length"
    def setLength2 (self, value):
        pass

    # Return float result [] from  type inputOutput field named "maxExtent"
    def getMaxExtent (self):
        pass

    # Assign float value [] to  type inputOutput field named "maxExtent"
    def setMaxExtent (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
        pass

    # Return X3DFontStyleNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fontStyle"
    def getFontStyle (self, result):
        pass

    # Assign X3DFontStyleNode value (using a properly typed node) to SFNode inputOutput field named "fontStyle"
    def setFontStyle1 (self, node):
        pass

    # Assign X3DFontStyleNode value (using a properly typed protoInstance)
    def setFontStyle2 (self, protoInstance):
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
