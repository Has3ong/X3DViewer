from . import *

# PixelTexture3D defines a concrete node interface that extends interface X3DTexture3DNode.
class CPixelTexture3D(CX3DTexture3DNode):
    m_strNodeName = "PixelTexture3D"
    def __init__(self):
        self.m_strNodeName = "PixelTexture3D"   
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return MFInt32 result [] from MFInt32 inputOutput field named "image"
    def getImage (self):
        pass

    # Return number of primitive values in "image" array
    def getNumImage (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "image"
    def setImage1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "image"
    def setImage2 (self, value):
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

    # Return boolean result from SFBool initializeOnly field named "repeatR"
    def getRepeatR (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "repeatR"
    def setRepeatR (self, value):
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
