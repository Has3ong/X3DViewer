from . import *

# X3DLightNode defines an abstract node interface that extends interfaces X3DNode.
# Light nodes provide illumination for rendering geometry in the scene.
class CX3DLightNode(CX3DChildNode):
    m_strNodeName = "X3DLightNode"
    def __init__(self):
        self.m_strNodeName = "X3DLightNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from intensityType type inputOutput field named "ambientIntensity"
    def getAmbientIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "ambientIntensity"
    def setAmbientIntensity (self, value) :
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "color"
    def setColor (self, color) :
        pass

    # Return float result [] from intensityType type inputOutput field named "intensity"
    def getIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "intensity"
    def setIntensity (self, value) :
        pass

    # Return bool result from SFBool inputOutput field named "on"
    def getOn (self):
        pass

    # Assign bool value to SFBool inputOutput field named "on"
    def setOn (self, value):
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