from . import *

# GeoOrigin defines a concrete node interface that extends interface X3DNode.
# GeoOrigin is deprecated and discouraged (but nevertheless allowed) in X3D v3.3.
class CGeoOrigin(CX3DNode):
    m_strNodeName = "GeoOrigin"
    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array [] from geoSystemType type initializeOnly field named "geoSystem"
    def getGeoSystem (self):
        pass

    # Return number of primitive values in "geoSystem" array
    def getNumGeoSystem (self):
        pass

    # Assign String array [] to geoSystemType type initializeOnly field named "geoSystem"
    def setGeoSystem (self, values, size):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "geoCoords"
    def getGeoCoords (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "geoCoords"
    def setGeoCoords (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "rotateYUp"
    def getRotateYUp (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "rotateYUp"
    def setRotateYUp (self, value):
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

 

