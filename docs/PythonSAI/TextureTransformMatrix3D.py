from . import *

# TextureTransformMatrix3D defines a concrete node interface that extends interface X3DTextureTransformNode.
class CTextureTransformMatrix3D(CX3DTextureTransformNode):
    m_strNodeName = "TextureTransformMatrix3D"
    def __init__(self):
        self.m_strNodeName = "TextureTransformMatrix3D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return array of float results array [] from SFMatrix4f inputOutput field named "matrix"
    def getMatrix (self):
        pass

    # Assign float array [] to SFMatrix4f inputOutput field named "matrix"
    def setMatrix (self, value):
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
