from . import *

# ComposedTexture3D defines a concrete node interface that extends interface X3DTexture3DNode.
class CComposedTexture3D(CX3DTexture3DNode):
    m_strNodeName = "ComposedTexture3D"
    def __init__(self):
        self.m_strNodeName = "ComposedTexture3D"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return array of X3DTexture2DNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "texture"
    def getTexture (self, result):
        pass

    # Return number of nodes in "texture" array
    def getNumTexture (self):
        pass

    # Assign X3DTexture2DNode array (using a properly typed node array) to MFNode inputOutput field named "texture"
    def setTexture1 (self, nodes):
        pass

    # Assign single X3DTexture2DNode value (using a properly typed node) as the MFNode array for inputOutput field named "texture"
    def setTexture2 (self, node):
        pass

    # Assign X3DTexture2DNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "texture"
    def setTexture3 (self, node):
        pass

    # Assign X3DTexture2DNode array (using a properly typed node array) to MFNode inputOutput field named "texture"
    def setTexture4 (self, nodes):
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
