from . import *

# Appearance defines a concrete node interface that extends interface X3DAppearanceNode.

class CAppearance(CX3DAppearanceNode):
    m_strNodeName = "Appearance"
    material = []
    texture = []
    textureTransform = []
    shaders = []

    def __init__(self):
        self.m_strNodeName = "Appearance"
        self.material = []
        self.texture = []
        self.textureTransform = []
        self.shaders = []
        
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    def setMaterial(self, node):
        self.material = node

    def setImageTexture(self, node):
        self.imagetexture = node

    # Return array of X3DShaderNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "shaders"
    def getShaders (self):
        pass

    # Return number of nodes in "shaders" array
    def getNumShaders (self):
        pass

    # Assign X3DShaderNode array (using a properly typed node array) to MFNode inputOutput field named "shaders"
    def setShaders1 (self, nodes, size):
        pass

    # Assign single X3DShaderNode value (using a properly typed node) as the MFNode array for inputOutput field named "shaders"
    def setShaders2 (self, node):
        pass

    # Assign X3DShaderNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "shaders"
    def setShaders3 (self, node):
        pass

    # Assign X3DShaderNode array (using a properly typed node array) to MFNode inputOutput field named "shaders"
    def setShaders4 (self, nodes, size):
        pass

    # Return FillProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fillProperties"
    def getFillProperties (self, result):
        pass

    # Assign FillProperties value (using a properly typed node) to SFNode inputOutput field named "fillProperties"
    def setFillProperties1 (self, node):
        pass

    # Assign FillProperties value (using a properly typed protoInstance)
    def setFillProperties2 (self, protoInstance):
        pass

    # Return LineProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "lineProperties"
    def getLineProperties (self, result):
        pass

    # Assign LineProperties value (using a properly typed node) to SFNode inputOutput field named "lineProperties"
    def setLineProperties1 (self, node):
        pass

    # Assign LineProperties value (using a properly typed protoInstance)
    def setLineProperties2 (self, protoInstance):
        pass

    # Return X3DMaterialNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "material"
    def getMaterial (self, result):
        pass

    # Assign X3DMaterialNode value (using a properly typed node) to SFNode inputOutput field named "material"
    def setMaterial1 (self, node):
        pass

    # Assign X3DMaterialNode value (using a properly typed protoInstance)
    def setMaterial2 (self, protoInstance):
        pass

    # Return X3DTextureNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "texture"
    def getTexture (self, result):
        pass

    # Assign X3DTextureNode value (using a properly typed node) to SFNode inputOutput field named "texture"
    def setTexture1 (self, node):
        pass

    # Assign X3DTextureNode value (using a properly typed protoInstance)
    def setTexture2 (self, protoInstance):
        pass

    # Return X3DTextureTransformNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "textureTransform"
    def getTextureTransform (self, result):
        pass

    # Assign X3DTextureTransformNode value (using a properly typed node) to SFNode inputOutput field named "textureTransform"
    def setTextureTransform1 (self, node):
        pass

    # Assign X3DTextureTransformNode value (using a properly typed protoInstance)
    def setTextureTransform2 (self, protoInstance):
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