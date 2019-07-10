from . import *

# GeoTouchSensor defines a concrete node interface that extends interface X3DTouchSensorNode.
class CGeoTouchSensor(CX3DTouchSensorNode):
    m_strNodeName = "GeoTouchSensor"
    def __init__(self):
        self.m_strNodeName = "GeoTouchSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "hitNormal_changed"
    def getHitNormal (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "hitPoint_changed"
    def getHitPoint (self):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f outputOnly field named "hitTexCoord_changed"
    def getHitTexCoord (self):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d outputOnly field named "hitGeoCoord_changed"
    def getHitGeoCoord (self):
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

    # Return boolean result from SFBool outputOnly field named "isOver"
    def getIsOver (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
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

    # Return double result in seconds from SFTime outputOnly field named "touchTime"
    def getTouchTime (self):
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
