from . import *

# TextureCoordinateGenerator defines a concrete node interface that extends interface X3DTextureCoordinateNode.
class CTextureCoordinateGenerator(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinateGenerator"
    def __init__(self):
        self.m_strNodeName = "TextureCoordinateGenerator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String enumeration result ("SPHERE"|"CAMERASPACENORMAL"|"CAMERASPACEPOSITION"|"CAMERASPACEREFLECTIONVECTOR"|"SPHERE-LOCAL"|"COORD"|"COORD-EYE"|"NOISE"|"NOISE-EYE"|"SPHERE-REFLECT"|"SPHERE-REFLECT-LOCAL") from textureCoordinateGeneratorModeValues type inputOutput field named "mode"
    def getMode (self):
        pass

    # Assign String enumeration value ("SPHERE"|"CAMERASPACENORMAL"|"CAMERASPACEPOSITION"|"CAMERASPACEREFLECTIONVECTOR"|"SPHERE-LOCAL"|"COORD"|"COORD-EYE"|"NOISE"|"NOISE-EYE"|"SPHERE-REFLECT"|"SPHERE-REFLECT-LOCAL") to textureCoordinateGeneratorModeValues type inputOutput field named "mode"
    def setMode (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "parameter"
    def getParameter (self):
        pass

    # Return number of primitive values in "parameter" array
    def getNumParameter (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "parameter"
    def setParameter1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "parameter"
    def setParameter2 (self, value):
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
