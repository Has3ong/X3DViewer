from . import *

# FontStyle defines a concrete node interface that extends interface X3DFontStyleNode.
class CFontStyle(CX3DFontStyleNode):
    m_strNodeName = "FontStyle"
    def __init__(self):
        self.m_strNodeName = "FontStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return array of String results array [] from MFString initializeOnly field named "family"
    def getFamily (self):
        pass

    # Return number of primitive values in "family" array
    def getNumFamily (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "family"
    def setFamily (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "family"
    def setFamily (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "horizontal"
    def getHorizontal (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "horizontal"
    def setHorizontal (self, value):
        pass

    # Return array of String results array [] from MFString initializeOnly field named "justify"
    def getJustify (self):
        pass

    # Return number of primitive values in "justify" array
    def getNumJustify (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "justify"
    def setJustify1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "justify"
    def setJustify2 (self, value):
        pass

    # Return String result [] from SFString initializeOnly field named "language"
    def getLanguage (self):
        pass

    # Assign String value [] to SFString initializeOnly field named "language"
    def setLanguage (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "leftToRight"
    def getLeftToRight (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "leftToRight"
    def setLeftToRight (self, value):
        pass

    # Return float result [] from SFFloat initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return float result [] from SFFloat initializeOnly field named "spacing"
    def getSpacing (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "spacing"
    def setSpacing (self, value):
        pass

    # Return String enumeration result ("PLAIN"|"BOLD"|"ITALIC"|"BOLDITALIC") from fontStyleValues type initializeOnly field named "style"
    def getStyle (self):
        pass

    # Assign String enumeration value ("PLAIN"|"BOLD"|"ITALIC"|"BOLDITALIC") to fontStyleValues type initializeOnly field named "style"
    def setStyle (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "topToBottom"
    def getTopToBottom (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "topToBottom"
    def setTopToBottom (self, value):
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
