from . import *

# TextureTransform defines a concrete node interface that extends interface X3DTextureTransformNode.
class CTextureTransfrom(CX3DTextureTransformNode):
    m_strNodeName = "TextureTransform"
    def __init__(self):
        self.m_strNodeName = "TextureTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "rotation"
    def getRotation (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "rotation"
    def setRotation (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "scale"
    def getScale (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "scale"
    def setScale (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "translation"
    def getTranslation (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "translation"
    def setTranslation (self, value):
        pass

    #  ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass