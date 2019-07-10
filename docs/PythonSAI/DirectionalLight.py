from . import *

# DirectionalLight defines a concrete node interface that extends interface X3DLightNode.
class CDirectionalLight(CX3DLightNode):
    m_strNodeName = "DirectionalLight"
    def __init__(self):
        self.m_strNodeName = "DirectionalLight"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "direction"
    def getDirection (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "direction"
    def setDirection (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "global"
    def getGlobal (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "global"
    def setGlobal (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return float result [] from intensityType type inputOutput field named "ambientIntensity"
    def getAmbientIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "ambientIntensity"
    def setAmbientIntensity (self, value):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "color"
    def setColor (self, color):
        pass

    # Return float result [] from intensityType type inputOutput field named "intensity"
    def getIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "intensity"
    def setIntensity (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "on"
    def getOn (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "on"
    def setOn (self, value):
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
