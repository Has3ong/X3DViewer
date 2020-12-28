from . import *

# Viewpoint defines a concrete node interface that extends interface X3DViewpointNode.
class CViewpoint(CX3DViewpointNode):
    m_strNodeName = "Viewpoint"
    CONST_PI = 3.14159265
    fieldOfView = CONST_PI / 4.0

    def __init__(self):
        self.m_strNodeName = "Viewpoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.CONST_PI = 3.14159265
        self.centerOfRotation = [0.0, 0.0, 0.0]
        self.fieldOfView = self.CONST_PI / 4.0

    # Return array of 3-tuple float results array in radians from SFVec3f inputOutput field named "centerOfRotation"
    def getCenterOfRotation (self):
        ret = CSFVec3f()
        ret.setValue3(self.centerOfRotation[0], self.centerOfRotation[1], self.centerOfRotation[2])

        return ret

    # Assign 3-tuple float array in radians to SFVec3f inputOutput field named "centerOfRotation"
    def setCenterOfRotation (self, value):
        self.centerOfRotation[0] = value.x()
        self.centerOfRotation[1] = value.y()
        self.centerOfRotation[2] = value.z()

    # Return float result [] from SFFloat inputOutput field named "fieldOfView"
    def getFieldOfView (self):
        return self.fieldOfView

    # Assign float value [] to SFFloat inputOutput field named "fieldOfView"
    def setFieldOfView (self, value):
        self.fieldOfView = value

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "position"
    def getPosition (self):
        ret = CSFVec3f()
        ret.setValue3(self.position[0], self.position[1], self.position[2])

        return ret

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "position"
    def setPosition (self, value):
        self.position[0] = value.x()
        self.position[1] = value.y()
        self.position[2] = value.z()

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
        return self.description

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        self.description = value

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

    def toX3DString(self):
        data = """%s orientation='%f %f %f' position='%f %f %f'"""%(
            self.m_strNodeName, self.orientation[0], self.orientation[1], self.orientation[2], self.position[0], self.position[1], self.position[2]
        )

        if self.description: data += """ description='%s'""" % (self.description)

        return data

