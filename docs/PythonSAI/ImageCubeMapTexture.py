from . import *

# ImageCubeMapTexture defines a concrete node interface that extends interfaces X3DEnvironmentTextureNodeX3DUrlObject.
class CImageCubeMapTexture(CX3DEnvironmentTextureNode, CX3DUrlObject):
    m_strNodeName = "CImageCubeMapTexture"
    def __init__(self):
        self.m_strNodeName = "CImageCubeMapTexture"
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
