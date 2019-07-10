from . import *

# NurbsPatchSurface defines a concrete node interface that extends interface X3DNurbsSurfaceGeometryNode.
class CNurbsPatchSurface(CX3DNurbsSurfaceGeometryNode):
    m_strNodeName = "NurbsPatchSurface"
    def __init__(self):
        self.m_strNodeName = "NurbsPatchSurface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool initializeOnly field named "uClosed"
    def getUClosed (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "uClosed"
    def setUClosed (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "vClosed"
    def getVClosed (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "vClosed"
    def setVClosed (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "uDimension"
    def getUDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "uDimension"
    def setUDimension (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "vDimension"
    def getVDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "vDimension"
    def setVDimension (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "uKnot"
    def getUKnot (self):
        pass

    # Return number of primitive values in "uKnot" array
    def getNumUKnot (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "uKnot"
    def setUKnot1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "uKnot"
    def setUKnot2 (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "vKnot"
    def getVKnot (self):
        pass

    # Return number of primitive values in "vKnot" array
    def getNumVKnot (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "vKnot"
    def setVKnot1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "vKnot"
    def setVKnot2 (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "uOrder"
    def getUOrder (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "uOrder"
    def setUOrder (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "vOrder"
    def getVOrder (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "vOrder"
    def setVOrder (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "uTessellation"
    def getUTessellation (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "uTessellation"
    def setUTessellation (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "vTessellation"
    def getVTessellation (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "vTessellation"
    def setVTessellation (self, value):
        pass

    # Return array of double results array [] from MFDouble inputOutput field named "weight"
    def getWeight (self):
        pass

    # Return number of primitive values in "weight" array
    def getNumWeight (self):
        pass

    # Assign double array [] to MFDouble inputOutput field named "weight"
    def setWeight (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for inputOutput field named "weight"
    def setWeight (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
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

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "controlPoint"
    def getControlPoint (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "controlPoint"
    def setControlPoint1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setControlPoint2 (self, protoInstance):
        pass

    # Return X3DTextureCoordinateNode|NurbsTextureCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "texCoord"
    def getTexCoord (self, result):
        pass

    # Assign X3DTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed node) to SFNode inputOutput field named "texCoord"
    def setTexCoord1 (self, node):
        pass

    # Assign X3DTextureCoordinateNode|NurbsTextureCoordinate value (using a properly typed protoInstance)
    def setTexCoord2 (self, protoInstance):
        pass
