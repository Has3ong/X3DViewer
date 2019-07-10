from . import *

# NurbsTrimmedSurface defines a concrete node interface that extends interface X3DNurbsSurfaceGeometryNode.
class CNurbsTrimmedSurface(CX3DNurbsSurfaceGeometryNode):
    m_strNodeName = "NurbsTrimmedSurface"
    def __init__(self):
        self.m_strNodeName = "NurbsTrimmedSurface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOnly field named "addTrimmingContour"
    def setAddTrimmingContour1 (self, nodes):
        pass

    # Assign single Contour2D value (using a properly typed node) as the MFNode array for inputOnly field named "addTrimmingContour"
    def setAddTrimmingContour2 (self, node):
        pass

    # Assign Contour2D array (using a properly typed protoInstance array) to MFNode inputOnly field named "addTrimmingContour"
    def setAddTrimmingContour3 (self, node):
        pass

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOnly field named "addTrimmingContour"
    def setAddTrimmingContour4 (self, nodes):
        pass

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOnly field named "removeTrimmingContour"
    def setRemoveTrimmingContour1 (self, nodes):
        pass

    # Assign single Contour2D value (using a properly typed node) as the MFNode array for inputOnly field named "removeTrimmingContour"
    def setRemoveTrimmingContour2 (self, node):
        pass

    # Assign Contour2D array (using a properly typed protoInstance array) to MFNode inputOnly field named "removeTrimmingContour"
    def setRemoveTrimmingContour3 (self, node):
        pass

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOnly field named "removeTrimmingContour"
    def setRemoveTrimmingContour4 (self, nodes):
        pass

    # Return array of Contour2D results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "trimmingContour"
    def getTrimmingContour (self, result):
        pass

    # Return number of nodes in "trimmingContour" array
    def getNumTrimmingContour (self):
        pass

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOutput field named "trimmingContour"
    def setTrimmingContour1 (self, nodes):
        pass

    # Assign single Contour2D value (using a properly typed node) as the MFNode array for inputOutput field named "trimmingContour"
    def setTrimmingContour2 (self, node):
        pass

    # Assign Contour2D array (using a properly typed protoInstance array) to MFNode inputOutput field named "trimmingContour"
    def setTrimmingContour3 (self, node):
        pass

    # Assign Contour2D array (using a properly typed node array) to MFNode inputOutput field named "trimmingContour"
    def setTrimmingContour4 (self, nodes):
        pass

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
    def setWeight1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for inputOutput field named "weight"
    def setWeight2 (self, value):
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
