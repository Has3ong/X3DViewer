from . import *

# GeoCoordinate defines a concrete node interface that extends interface X3DCoordinateNode.
class CGeoCoordinate(CX3DCoordinateNode):
    m_strNodeName = "GeoCoordinate"
    def __init__(self):
        self.m_strNodeName = "GeoCoordinate"
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

    # Return array of 3-tuple double results array [] from MFVec3d initializeOnly field named "point"
    def getPoint (self):
        pass

    # Return number of 3-tuple primitive values in "point" array
    def getNumPoint (self):
        pass

    # Assign 3-tuple double array [] to MFVec3d initializeOnly field named "point"
    def setPoint (self, values, size):
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
