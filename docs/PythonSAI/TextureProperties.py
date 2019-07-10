from . import *

# TextureProperties defines a concrete node interface that extends interface X3DNode.
class CTextureProperties(CX3DNode):
    m_strNodeName = "TextureProperties"
    def __init__(self):
        self.m_strNodeName = "TextureProperties"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "anisotropicDegree"
    def getAnisotropicDegree (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "anisotropicDegree"
    def setAnisotropicDegree (self, value):
        pass

    # Return array of 4-tuple float results array using RGBA values [0..1] from SFColorRGBA inputOutput field named "borderColor"
    def getBorderColor (self):
        pass

    # Assign 4-tuple float array using RGBA values [0..1] to SFColorRGBA inputOutput field named "borderColor"
    def setBorderColor (self, color):
        pass

    # Return int result [] from SFInt32 inputOutput field named "borderWidth"
    def getBorderWidth (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "borderWidth"
    def setBorderWidth (self, value):
        pass

    # Return String enumeration result ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") from textureBoundaryModeValues type inputOutput field named "boundaryModeS"
    def getBoundaryModeS (self):
        pass

    # Assign String enumeration value ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") to textureBoundaryModeValues type inputOutput field named "boundaryModeS"
    def setBoundaryModeS (self, value):
        pass

    # Return String enumeration result ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") from textureBoundaryModeValues type inputOutput field named "boundaryModeT"
    def getBoundaryModeT (self):
        pass

    # Assign String enumeration value ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") to textureBoundaryModeValues type inputOutput field named "boundaryModeT"
    def setBoundaryModeT (self, value):
        pass

    # Return String enumeration result ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") from textureBoundaryModeValues type inputOutput field named "boundaryModeR"
    def getBoundaryModeR (self):
        pass

    # Assign String enumeration value ("CLAMP"|"CLAMP_TO_EDGE"|"CLAMP_TO_BOUNDARY"|"MIRRORED_REPEAT"|"REPEAT") to textureBoundaryModeValues type inputOutput field named "boundaryModeR"
    def setBoundaryModeR (self, value):
        pass

    # Return String enumeration result ("AVG_PIXEL"|"DEFAULT"|"FASTEST"|"NEAREST_PIXEL"|"NICEST") from textureMagnificationModeValues type inputOutput field named "magnificationFilter"
    def getMagnificationFilter (self):
        pass

    # Assign String enumeration value ("AVG_PIXEL"|"DEFAULT"|"FASTEST"|"NEAREST_PIXEL"|"NICEST") to textureMagnificationModeValues type inputOutput field named "magnificationFilter"
    def setMagnificationFilter (self, value):
        pass

    # Return String enumeration result ("AVG_PIXEL"|"AVG_PIXEL_AVG_MIPMAP"|"AVG_PIXEL_NEAREST_MIPMAP"|"DEFAULT"|"FASTEST"|"NEAREST_PIXEL"|"NEAREST_PIXEL_AVG_MIPMAP"|"NEAREST_PIXEL_NEAREST_MIPMAP"|"NICEST") from textureMinificationModeValues type inputOutput field named "minificationFilter"
    def getMinificationFilter (self):
        pass

    # Assign String enumeration value ("AVG_PIXEL"|"AVG_PIXEL_AVG_MIPMAP"|"AVG_PIXEL_NEAREST_MIPMAP"|"DEFAULT"|"FASTEST"|"NEAREST_PIXEL"|"NEAREST_PIXEL_AVG_MIPMAP"|"NEAREST_PIXEL_NEAREST_MIPMAP"|"NICEST") to textureMinificationModeValues type inputOutput field named "minificationFilter"
    def setMinificationFilter (self, value):
        pass

    # Return String enumeration result ("DEFAULT"|"FASTEST"|"HIGH"|"LOW"|"MEDIUM"|"NICEST") from textureCompressionModeValues type inputOutput field named "textureCompression"
    def getTextureCompression (self):
        pass

    # Assign String enumeration value ("DEFAULT"|"FASTEST"|"HIGH"|"LOW"|"MEDIUM"|"NICEST") to textureCompressionModeValues type inputOutput field named "textureCompression"
    def setTextureCompression (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "texturePriority"
    def getTexturePriority (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "texturePriority"
    def setTexturePriority (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "generateMipMaps"
    def getGenerateMipMaps (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "generateMipMaps"
    def setGenerateMipMaps (self, value):
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
