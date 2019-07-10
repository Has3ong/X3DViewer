from . import *

# TwoSidedMaterial defines a concrete node interface that extends interface X3DMaterialNode.
class CTwoSidedMaterial(CX3DNode):
    m_strNodeName = "TwoSidedMaterial"
    def __init__(self):
        self.m_strNodeName = "TwoSidedMaterial"
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
    def setAmbientIntensity (self, value):
        pass

    # Return float result [] from intensityType type inputOutput field named "backAmbientIntensity"
    def getBackAmbientIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "backAmbientIntensity"
    def setBackAmbientIntensity (self, value):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "diffuseColor"
    def getDiffuseColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "diffuseColor"
    def setDiffuseColor (self, color):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "backDiffuseColor"
    def getBackDiffuseColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "backDiffuseColor"
    def setBackDiffuseColor (self, color):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "emissiveColor"
    def getEmissiveColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "emissiveColor"
    def setEmissiveColor (self, color):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "backEmissiveColor"
    def getBackEmissiveColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "backEmissiveColor"
    def setBackEmissiveColor (self, color):
        pass

    # Return float result [] from intensityType type inputOutput field named "shininess"
    def getShininess (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "shininess"
    def setShininess (self, value):
        pass

    # Return float result [] from intensityType type inputOutput field named "backShininess"
    def getBackShininess (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "backShininess"
    def setBackShininess (self, value):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "specularColor"
    def getSpecularColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "specularColor"
    def setSpecularColor (self, color):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "backSpecularColor"
    def getBackSpecularColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "backSpecularColor"
    def setBackSpecularColor (self, color):
        pass

    # Return float result [] from intensityType type inputOutput field named "transparency"
    def getTransparency (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "transparency"
    def setTransparency (self, value):
        pass

    # Return float result [] from intensityType type inputOutput field named "backTransparency"
    def getBackTransparency (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "backTransparency"
    def setBackTransparency (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "separateBackColor"
    def getSeparateBackColor (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "separateBackColor"
    def setSeparateBackColor (self, color):
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
