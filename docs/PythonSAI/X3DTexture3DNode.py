from . import *

# X3DTexture3DNode defines an abstract node interface that extends interfaces X3DAppearanceChildNode, X3DNode
class CX3DTexture3DNode(CX3DTextureNode):
    m_strNodeName = "X3DTexture3DNode"
    def __init__(self):
        self.m_strNodeName = "X3DTexture3DNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return bool result from SFBool initializeOnly field named "repeatS"
    def getRepeatS (self):
        pass

    # Assign bool value to SFBool initializeOnly field named "repeatS"
    def setRepeatS (self, value):
        pass

    # Return bool result from SFBool initializeOnly field named "repeatT"
    def getRepeatT (self):
        pass

    # Assign bool value to SFBool initializeOnly field named "repeatT"
    def setRepeatT (self, value):
        pass

    # Return bool result from SFBool initializeOnly field named "repeatR"
    def getRepeatR (self):
        pass

    # Assign bool value to SFBool initializeOnly field named "repeatR"
    def setRepeatR (self, value):
        pass

    # Return TextureProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "textureProperties"
    def getTextureProperties (self, result):
        pass

    # Assign TextureProperties value (using a properly typed node) to SFNode initializeOnly field named "textureProperties"
    def setTextureProperties1 (self, node) :
        pass

    # Assign TextureProperties value (using a properly typed protoInstance)
    def setTextureProperties2 (self, protoInstance) :
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