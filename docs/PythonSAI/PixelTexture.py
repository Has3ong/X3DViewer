from . import *

# PixelTexture defines a concrete node interface that extends interface X3DTexture2DNode.
class CPixelTexture(CX3DTexture2DNode):
    m_strNodeName = "CPix3lTexture"
    def __init__(self):
        self.m_strNodeName = "PixelTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return SFImage result [] from SFImage inputOutput field named "image"
    def getImage (self):
        pass

    # Assign SFImage value [] to SFImage inputOutput field named "image"
    def setImage (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool initializeOnly field named "repeatS"
    def getRepeatS (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "repeatS"
    def setRepeatS (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "repeatT"
    def getRepeatT (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "repeatT"
    def setRepeatT (self, value):
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

    # Return TextureProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "textureProperties"
    def getTextureProperties (self, result):
        pass

    # Assign TextureProperties value (using a properly typed node) to SFNode initializeOnly field named "textureProperties"
    def setTextureProperties1 (self, node):
        pass

    # Assign TextureProperties value (using a properly typed protoInstance)
    def setTextureProperties2 (self, protoInstance):
        pass
