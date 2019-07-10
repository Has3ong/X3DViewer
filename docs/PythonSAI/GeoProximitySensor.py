from . import *

# GeoProximitySensor defines a concrete node interface that extends interface X3DEnvironmentalSensorNode.
class CGeoProximitySensor(CX3DEnviromentalSensorNode):
    m_strNodeName = "GeoProximitySensor"
    def __init__(self):
        self.m_strNodeName = "GeoProximitySensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array in radians from SFVec3f outputOnly field named "centerOfRotation_changed"
    def getCenterOfRotation (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "enterTime"
    def getEnterTime (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "exitTime"
    def getExitTime (self):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d outputOnly field named "geoCoord_changed"
    def getGeoCoord (self, result):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation outputOnly field named "orientation_changed"
    def getOrientation (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "position_changed"
    def getPosition (self):
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

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "geoCenter"
    def getGeoCenter (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "geoCenter"
    def setGeoCenter (self, value):
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

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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
