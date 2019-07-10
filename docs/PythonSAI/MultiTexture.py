from . import *

# MultiTexture defines a concrete node interface that extends interface X3DTextureNode.
class CMultiTexture(CX3DTextureNode):
    m_strNodeName = "MultiTexture"
    def __init__(self):
        self.m_strNodeName = "MultiTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "alpha"
    def getAlpha (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "alpha"
    def setAlpha (self, value):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "color"
    def setColor (self, color):
        pass

    # Return array of String results array [] from MFString inputOutput field named "function"
    def getFunction (self):
        pass

    # Return number of primitive values in "function" array
    def getNumFunction (self):
        pass

    # Assign String array [] to MFString inputOutput field named "function"
    def setFunction1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "function"
    def setFunction2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "mode"
    def getMode (self):
        pass

    # Return number of primitive values in "mode" array
    def getNumMode (self):
        pass

    # Assign String array [] to MFString inputOutput field named "mode"
    def setMode1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "mode"
    def setMode2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "source"
    def getSource (self):
        pass

    # Return number of primitive values in "source" array
    def getNumSource (self):
        pass

    # Assign String array [] to MFString inputOutput field named "source"
    def setSource1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "source"
    def setSource2 (self, value):
        pass

    # Return array of X3DTextureNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "texture"
    def getTexture (self, result):
        pass

    # Return number of nodes in "texture" array
    def getNumTexture (self):
        pass

    # Assign X3DTextureNode array (using a properly typed node array) to MFNode inputOutput field named "texture"
    def setTexture1 (self, nodes):
        pass

    # Assign single X3DTextureNode value (using a properly typed node) as the MFNode array for inputOutput field named "texture"
    def setTexture2 (self, node):
        pass

    # Assign X3DTextureNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "texture"
    def setTexture (self, node):
        pass

    # Assign X3DTextureNode array (using a properly typed node array) to MFNode inputOutput field named "texture"
    def setTexture (self, nodes):
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
