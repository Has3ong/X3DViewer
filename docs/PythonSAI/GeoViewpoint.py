from . import *

# GeoViewpoint defines a concrete node interface that extends interface X3DViewpointNode.
class CGeoViewpoint(CX3DBindableNode):
    m_strNodeName = "GeoViewpoint"
    def __init__(self):
        self.m_strNodeName = "GeoViewpoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple double results array in radians from SFVec3d inputOutput field named "centerOfRotation"
    def getCenterOfRotation (self):
        pass

    # Assign 3-tuple double array in radians to SFVec3d inputOutput field named "centerOfRotation"
    def setCenterOfRotation (self, value):
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

    # Return float result [] from SFFloat inputOutput field named "fieldOfView"
    def getFieldOfView (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "fieldOfView"
    def setFieldOfView (self, value):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "position"
    def getPosition (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "position"
    def setPosition (self, value):
        pass

    # Return float result [] from SFFloat initializeOnly field named "speedFactor"
    def getSpeedFactor (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "speedFactor"
    def setSpeedFactor (self, value):
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

    # Assign boolean value to SFBool inputOnly field named "set_bind"
    def setBind (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isBound"
    def getIsBound (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "jump"
    def getJump (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "jump"
    def setJump (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "orientation"
    def getOrientation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "orientation"
    def setOrientation (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "retainUserOffsets"
    def getRetainUserOffsets (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "retainUserOffsets"
    def setRetainUserOffsets (self, value):
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
