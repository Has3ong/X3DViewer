from . import *

# CylinderSensor defines a concrete node interface that extends interface X3DDragSensorNode.
class CCylinderSensor(CX3DDragSensorNode):
    m_strNodeName = "CylinderSensor"
    def __init__(self):
        self.m_strNodeName = "CylinderSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 4-tuple float results array in radians from SFRotation outputOnly field named "rotation_changed"
    def getRotation (self):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "axisRotation"
    def getAxisRotation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "axisRotation"
    def setAxisRotation (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "diskAngle"
    def getDiskAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "diskAngle"
    def setDiskAngle (self, angle):
        pass

    # Return float result in radians from SFFloat inputOutput field named "maxAngle"
    def getMaxAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "maxAngle"
    def setMaxAngle (self, angle):
        pass

    # Return float result in radians from SFFloat inputOutput field named "minAngle"
    def getMinAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "minAngle"
    def setMinAngle (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "offset"
    def getOffset (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "offset"
    def setOffset (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "trackPoint_changed"
    def getTrackPoint (self):
        pass

    # Return boolean result from SFBool inputOutput field named "autoOffset"
    def getAutoOffset (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "autoOffset"
    def setAutoOffset (self, value):
        pass

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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
