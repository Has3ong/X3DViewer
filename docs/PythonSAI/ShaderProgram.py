from . import *

# ShaderProgram defines a concrete node interface that extends interfaces X3DNodeMixedContentX3DProgrammableShaderObject, X3DUrlObject.
# ShaderProgram can contain field declarations and a CDATA section of plain-text source code.
class CShaderProgram(CX3DUrlObject, CX3DProgrammableShaderObject):
    m_strNodeName = "ShaderProgram"
    def __init__(self):
        self.m_strNodeName = "ShaderProgram"
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

    # Return String enumeration result ("VERTEX"|"FRAGMENT") from shaderPartTypeValues type initializeOnly field named "type"
    def getType (self):
        pass

    # Assign String enumeration value ("VERTEX"|"FRAGMENT") to shaderPartTypeValues type initializeOnly field named "type"
    def setType (self, value):
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
