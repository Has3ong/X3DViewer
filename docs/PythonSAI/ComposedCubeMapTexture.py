from . import *

# ComposedCubeMapTexture defines a concrete node interface that extends interface X3DEnvironmentTextureNode.
class CComposedCubeMapTexture(CX3DEnvironmentTextureNode):
    m_strNodeName = "ComposedCubeMapTexture"
    def __init__(self):
        self.m_strNodeName = "ComposedCubeMapTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "back"
    def getBack (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "back"
    def setBack (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setBack (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "bottom"
    def getBottom (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "bottom"
    def setBottom (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setBottom (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "front"
    def getFront (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "front"
    def setFront (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setFront (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "left"
    def getLeft (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "left"
    def setLeft (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setLeft (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "right"
    def getRight (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "right"
    def setRight (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setRight (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "top"
    def getTop (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "top"
    def setTop (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setTop (self, protoInstance):
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
