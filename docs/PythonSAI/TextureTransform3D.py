from . import *

# TextureTransform3D defines a concrete node interface that extends interface X3DTextureTransformNode.
class CTextureTransform3D(CX3DTextureTransformNode):
    m_strNodeName = "TextureTransform3D"
    def __init__(self):
        self.m_strNodeName = "TextureTransform3D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "rotation"
    def getRotation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "rotation"
    def setRotation (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "scale"
    def getScale (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "scale"
    def setScale (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "translation"
    def getTranslation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "translation"
    def setTranslation (self, value):
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
