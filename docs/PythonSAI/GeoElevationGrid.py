from . import *

# GeoElevationGrid defines a concrete node interface that extends interface X3DGeometryNode.
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
    def setHeight (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOnly field named "set_height"
    def setHeight (self, value):
        pass

    # Return array of String results array [] from geoSystemType type initializeOnly field named "geoSystem"
    def getGeoSystem (self):
        pass

    # Return number of primitive values in "geoSystem" array
    def getNumGeoSystem (self):
        pass

    # Assign String array [] to geoSystemType type initializeOnly field named "geoSystem"
    def setGeoSystem (self, values, size):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d initializeOnly field named "geoGridOrigin"
    def getGeoGridOrigin (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d initializeOnly field named "geoGridOrigin"
    def setGeoGridOrigin (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "height"
    def getHeight (self):
        pass

    # Return number of primitive values in "height" array
    def getNumHeight (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "height"
    def setHeight (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "height"
    def setHeight (self, value):
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

    # Return double result [] from  type initializeOnly field named "xSpacing"
    def getXSpacing (self):
        pass

    # Assign double value [] to  type initializeOnly field named "xSpacing"
    def setXSpacing (self, value):
        pass

    # Return float result [] from  type inputOutput field named "yScale"
    def getYScale (self):
        pass

    # Assign float value [] to  type inputOutput field named "yScale"
    def setYScale (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "zDimension"
    def getZDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "zDimension"
    def setZDimension (self, value):
        pass

    # Return double result [] from  type initializeOnly field named "zSpacing"
    def getZSpacing (self):
        pass

    # Assign double value [] to  type initializeOnly field named "zSpacing"
    def setZSpacing (self, value):
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

    # Return X3DNormalNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "normal"
    def getNormal (self, result):
        pass

    # Assign X3DNormalNode value (using a properly typed node) to SFNode inputOutput field named "normal"
    def setNormal1 (self, node):
        pass

    # Assign X3DNormalNode value (using a properly typed protoInstance)
    def setNormal2 (self, protoInstance):
        pass

    # Return GeoOrigin result (deprecated node, optional) from SFNode initializeOnly field named "geoOrigin"
    def getGeoOrigin (self, result):
        pass

    # Assign GeoOrigin value (deprecated node, optional) to SFNode initializeOnly field named "geoOrigin"
    def setGeoOrigin1 (self, node):
        pass

    # Assign GeoOrigin value (deprecated protoInstance)
    def setGeoOrigin2 (self, protoInstance):
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
