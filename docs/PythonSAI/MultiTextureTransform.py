from . import *

# MultiTextureTransform defines a concrete node interface that extends interface X3DTextureTransformNode.
class CMultiTextureTransform(CX3DTextureTransformNode):
    m_strNodeName = "MultiTextureTransform"
    def __init__(self):
        self.m_strNodeName = "MultiTextureTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of X3DTextureTransformNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "textureTransform"
    def getTextureTransform (self, result):
        pass

    # Return number of nodes in "textureTransform" array
    def getNumTextureTransform (self):
        pass

    # Assign X3DTextureTransformNode array (using a properly typed node array) to MFNode inputOutput field named "textureTransform"
    def setTextureTransform1 (self, nodes):
        pass

    # Assign single X3DTextureTransformNode value (using a properly typed node) as the MFNode array for inputOutput field named "textureTransform"
    def setTextureTransform2 (self, node):
        pass

    # Assign X3DTextureTransformNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "textureTransform"
    def setTextureTransform3 (self, node):
        pass

    # Assign X3DTextureTransformNode array (using a properly typed node array) to MFNode inputOutput field named "textureTransform"
    def setTextureTransform4 (self, nodes):
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