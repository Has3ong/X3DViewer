from . import *

# ComposedShader defines a concrete node interface that extends interfaces X3DShaderNode, X3DProgrammableShaderObject.
# ComposedShader can contain field declarations, but no CDATA section of plain-text source code, since programs are composed from child ShaderPart nodes.
class CComposedShader(CX3DShaderNode, CX3DProgrammableShaderObject):
    m_strNodeName = "ComposedShader"
    def __init__(self):
        self.m_strNodeName = "ComposedShader"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

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

    # Return array of ShaderPart results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "parts"
    def getParts (self, result):
        pass

    # Return number of nodes in "parts" array
    def getNumParts (self):
        pass

    # Assign ShaderPart array (using a properly typed node array) to MFNode inputOutput field named "parts"
    def setParts1 (self, nodes):
        pass

    # Assign single ShaderPart value (using a properly typed node) as the MFNode array for inputOutput field named "parts"
    def setParts2 (self, node):
        pass

    # Assign ShaderPart array (using a properly typed protoInstance array) to MFNode inputOutput field named "parts"
    def setParts3 (self, node):
        pass

    # Assign ShaderPart array (using a properly typed node array) to MFNode inputOutput field named "parts"
    def setParts4 (self, nodes):
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
