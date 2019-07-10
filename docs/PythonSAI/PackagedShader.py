from . import *

# PackagedShader defines a concrete node interface that extends interfaces X3DShaderNodeX3DUrlObject, X3DProgrammableShaderObject.
# PackagedShader can contain field declarations, but no CDATA section of plain-text source code.
class CPackagedShader(CX3DShaderNode, CX3DUrlObject, CX3DProgrammableShaderObject):
    m_strNodeName = "PackagedShader"
    def __init__(self):
        self.m_strNodeName = "PackagedShader"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getUrl (self):
        pass

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Assign boolean value to SFBool inputOnly field named "activate"
    def setActivate (self, value):
        pass

    # Return boolean result from SFBool outputOnly field named "isSelected"
    def getIsSelected (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isValid"
    def getIsValid (self):
        pass

    # Return String result (enumeration values = "Cg"|"GLSL"|"HLSL"|...) from SFString initializeOnly field named "language"
    def getLanguage (self):
        pass

    # Assign String value (enumeration values = "Cg"|"GLSL"|"HLSL"|...) to SFString initializeOnly field named "language"
    def setLanguage (self, value):
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
