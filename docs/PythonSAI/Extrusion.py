from . import *

# Extrusion defines a concrete node interface that extends interface X3DGeometryNode.
class CExtrusion(CX3DGeometryNode):
    m_strNodeName = "Extrusion"
    def __init__(self):
        self.m_strNodeName = "Extrusion"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Assign 2-tuple float array [] to MFVec2f inputOnly field named "set_crossSection"
    def setCrossSection (self, values, size):
        pass

    # Assign 4-tuple float array in radians to MFRotation inputOnly field named "set_orientation"
    def setOrientation (self, values, size):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOnly field named "set_scale"
    def setScale (selfe, values, size):
        pass

    # Assign 3-tuple float array [] to MFVec3f inputOnly field named "set_spine"
    def setSpine (self, values, size):
        pass

    # Return boolean result from SFBool initializeOnly field named "beginCap"
    def getBeginCap (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "beginCap"
    def setBeginCap (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "ccw"
    def getCcw (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "ccw"
    def setCcw (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "convex"
    def getConvex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "convex"
    def setConvex (self, value):
        pass

    # Return float result in radians from  type initializeOnly field named "creaseAngle"
    def getCreaseAngle (self):
        pass

    # Assign float value in radians to  type initializeOnly field named "creaseAngle"
    def setCreaseAngle (self, angle):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f initializeOnly field named "crossSection"
    def getCrossSection (self):
        pass

    # Return number of 2-tuple primitive values in "crossSection" array
    def getNumCrossSection (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f initializeOnly field named "crossSection"
    def setCrossSection (self, values, size):
        pass

    # Return boolean result from SFBool initializeOnly field named "endCap"
    def getEndCap (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "endCap"
    def setEndCap (self, value):
        pass

    # Return array of 4-tuple float results array in radians from MFRotation initializeOnly field named "orientation"
    def getOrientation (self):
        pass

    # Return number of 4-tuple primitive values in "orientation" array
    def getNumOrientation (self):
        pass

    # Assign 4-tuple float array in radians to MFRotation initializeOnly field named "orientation"
    def setOrientation (self, values, size):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f initializeOnly field named "scale"
    def getScale (self):
        pass

    # Return number of 2-tuple primitive values in "scale" array
    def getNumScale (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f initializeOnly field named "scale"
    def setScale (selfe, values, size):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f initializeOnly field named "spine"
    def getSpine (self):
        pass

    # Return number of 3-tuple primitive values in "spine" array
    def getNumSpine (self):
        pass

    # Assign 3-tuple float array [] to MFVec3f initializeOnly field named "spine"
    def setSpine (self, values, size):
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
