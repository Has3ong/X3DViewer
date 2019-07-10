from . import *

# GeneratedCubeMapTexture defines a concrete node interface that extends interface X3DEnvironmentTextureNode.
class CGeneratedCubeMapTexture(CX3DEnvironmentTextureNode):
    m_strNodeName = "GeneratedCubeMapTexture"
    def __init__(self):
        self.m_strNodeName = "GeneratedCubeMapTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result ["NONE"|"NEXT_FRAME_ONLY"|"ALWAYS"] from  type inputOutput field named "update"
    def getUpdate (self):
        pass

    # Assign String value ["NONE"|"NEXT_FRAME_ONLY"|"ALWAYS"] to  type inputOutput field named "update"
    def setUpdate (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign int value [] to  type initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return TextureProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "textureProperties"
    def getTextureProperties (self, result):
        pass

    # Assign TextureProperties value (using a properly typed node) to SFNode initializeOnly field named "textureProperties"
    def setTextureProperties1 (self, node):
        pass

    # Assign TextureProperties value (using a properly typed protoInstance)
    def setTextureProperties2 (self, protoInstance):
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
