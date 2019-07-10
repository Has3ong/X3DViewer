from . import *

# ProximitySensor defines a concrete node interface that extends interface X3DEnvironmentalSensorNode.
class CProximitySensor(CX3DEnviromentalSensorNode):
    m_strNodeName = "ProximitySensor"
    def __init__(self):
        self.m_strNodeName = "ProximitySensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return double result in seconds from SFTime outputOnly field named "enterTime"
    def getEnterTime (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "exitTime"
    def getExitTime (self):
        pass

    # Return array of 3-tuple float results array in radians from SFVec3f outputOnly field named "centerOfRotation_changed"
    def getCenterOfRotation (self):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation outputOnly field named "orientation_changed"
    def getOrientation (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "position_changed"
    def getPosition (self):
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