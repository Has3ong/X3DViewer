from . import *

# ProgramShader defines a concrete node interface that extends interface X3DShaderNode.
# ProgramShader contains no field declarations and no plain-text source code.
class CProgramShader(CX3DShaderNode):
    m_strNodeName = "ProgramShader"
    def __init__(self):
        self.m_strNodeName = "ProgramShader"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of ShaderProgram results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "programs"
    def getPrograms (self, result):
        pass

    # Return number of nodes in "programs" array
    def getNumPrograms (self):
        pass

    # Assign ShaderProgram array (using a properly typed node array) to MFNode inputOutput field named "programs"
    def setPrograms1 (self, nodes):
        pass

    # Assign single ShaderProgram value (using a properly typed node) as the MFNode array for inputOutput field named "programs"
    def setPrograms2 (self, node):
        pass

    # Assign ShaderProgram array (using a properly typed protoInstance array) to MFNode inputOutput field named "programs"
    def setPrograms3 (self, node):
        pass

    # Assign ShaderProgram array (using a properly typed node array) to MFNode inputOutput field named "programs"
    def setPrograms4 (self, nodes):
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
