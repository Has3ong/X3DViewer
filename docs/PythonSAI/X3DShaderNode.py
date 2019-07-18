from . import *

# X3DShaderNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DShaderNode(CX3DAppearanceChildNode):
    m_strNodeName = "X3DShaderNode"
    def __init__(self):
        self.m_strNodeName = "X3DShaderNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign bool value to SFBool inputOnly field named "activate"
    def setActivate (self, value):
        pass

    # Return bool result from SFBool outputOnly field named "isSelected"
    def getIsSelected (self):
        pass

    # Return bool result from SFBool outputOnly field named "isValid"
    def getIsValid (self):
        pass

    # Return String result (enumeration values = "Cg"|"GLSL"|"HLSL"|...) from SFString initializeOnly field named "language"
    def getLanguage (self):
        pass

    # Assign String value (enumeration values = "Cg"|"GLSL"|"HLSL"|...) to SFString initializeOnly field named "language"
    def setLanguage (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass