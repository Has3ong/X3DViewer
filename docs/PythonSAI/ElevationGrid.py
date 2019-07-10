from . import *

# ElevationGrid defines a concrete node interface that extends interface X3DGeometryNode.
class CElevationGrid(CX3DGeometryNode):
    m_strNodeName = "ElevationGrid"
    def __init__(self):
        self.m_strNodeName = "ElevationGrid"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign float array [] to MFFloat inputOnly field named "set_height"
    def setHeight1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOnly field named "set_height"
    def setHeight2 (self, value):
        pass

    # Return array of float results array [] from MFFloat initializeOnly field named "height"
    def getHeight (self):
        pass

    # Return number of primitive values in "height" array
    def getNumHeight (self):
        pass

    # Assign float array [] to MFFloat initializeOnly field named "height"
    def setHeight3 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for initializeOnly field named "height"
    def setHeight4 (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "ccw"
    def getCcw (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "ccw"
    def setCcw (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "colorPerVertex"
    def getColorPerVertex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "colorPerVertex"
    def setColorPerVertex (self, color):
        pass

    # Return float result in radians from  type initializeOnly field named "creaseAngle"
    def getCreaseAngle (self):
        pass

    # Assign float value in radians to  type initializeOnly field named "creaseAngle"
    def setCreaseAngle (self, angle):
        pass

    # Return boolean result from SFBool initializeOnly field named "normalPerVertex"
    def getNormalPerVertex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "normalPerVertex"
    def setNormalPerVertex (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "xDimension"
    def getXDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "xDimension"
    def setXDimension (self, value):
        pass

    # Return float result [] from  type initializeOnly field named "xSpacing"
    def getXSpacing (self):
        pass

    # Assign float value [] to  type initializeOnly field named "xSpacing"
    def setXSpacing (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "zDimension"
    def getZDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "zDimension"
    def setZDimension (self, value):
        pass

    # Return float result [] from  type initializeOnly field named "zSpacing"
    def getZSpacing (self):
        pass

    # Assign float value [] to  type initializeOnly field named "zSpacing"
    def setZSpacing (self, value):
        pass

    # Return array of X3DVertexAttributeNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "attrib"
    def getAttrib (self, result):
        pass

    # Return number of nodes in "attrib" array
    def getNumAttrib (self):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib1 (self, nodes):
        pass

    # Assign single X3DVertexAttributeNode value (using a properly typed node) as the MFNode array for inputOutput field named "attrib"
    def setAttrib2 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "attrib"
    def setAttrib3 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib4 (self, nodes):
        pass

    # Return X3DColorNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "color"
    def getColor (self, result):
        pass

    # Assign X3DColorNode value (using a properly typed node) to SFNode inputOutput field named "color"
    def setColor1 (self, color):
        pass

    # Assign X3DColorNode value (using a properly typed protoInstance)
    def setColor2 (self, protoInstance):
        pass

    # Return FogCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fogCoord"
    def getFogCoord (self, result):
        pass

    # Assign FogCoordinate value (using a properly typed node) to SFNode inputOutput field named "fogCoord"
    def setFogCoord1 (self, node):
        pass

    # Assign FogCoordinate value (using a properly typed protoInstance)
    def setFogCoord2 (self, protoInstance):
        pass

    # Return X3DNormalNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "normal"
    def getNormal (self, result):
        pass

    # Assign X3DNormalNode value (using a properly typed node) to SFNode inputOutput field named "normal"
    def setNormal1 (self, node):
        pass

    # Assign X3DNormalNode value (using a properly typed protoInstance)
    def setNormal2 (self, protoInstance):
        pass

    # Return X3DTextureCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "texCoord"
    def getTexCoord (self, result):
        pass

    # Assign X3DTextureCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "texCoord"
    def setTexCoord1 (self, node):
        pass

    # Assign X3DTextureCoordinateNode value (using a properly typed protoInstance)
    def setTexCoord2 (self, protoInstance):
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