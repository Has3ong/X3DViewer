from . import *

# X3DViewpointNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
class CX3DViewpointNode(CX3DNode):
    m_strNodeName= "X3DViewpointNode"
    jump = True
    retainUserOffsets = False
    position = [0.0, 0.0, 10.0]
    orientation = [0.0, 0.0, 1.0, 0.0]
    centerOfRotation = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_strNodeName = "X3DViewpointNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.jump = True
        self.retainUserOffsets = False
        self.position = [0.0, 0.0, 10.0]
        self.orientation = [0.0, 0.0, 1.0, 0.0]
        self.centerOfRotation = [0.0, 0.0, 0.0]

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription(self):
        return self.description

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription(self, value):
        self.description = value

    # Return bool result from SFBool inputOutput field named "jump"
    def getJump(self):
        return self.jump

    # Assign bool value to SFBool inputOutput field named "jump"
    def setJump(self, value):
        self.jump = value

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "orientation"
    def getOrientation(self):
        ret = CSFRotation()
        ret.setValue4(self.orientation[0], self.orientation[1], self.orientation[2], self.orientation[3])

        return ret

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "orientation"
    def setOrientation(self, value):
        self.orientation[0] = value.x()
        self.orientation[1] = value.y()
        self.orientation[2] = value.z()
        self.orientation[3] = value.w()

    # Return bool result from SFBool inputOutput field named "retainUserOffsets"
    def getRetainUserOffsets(self):
        return self.retainUserOffsets

    # Assign bool value to SFBool inputOutput field named "retainUserOffsets"
    def setRetainUserOffsets(self, value):
        self.retainUserOffsets = value

    # Assign bool value to SFBool inputOnly field named "set_bind"
    def setBind(self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime(self):
        pass

    # Return bool result from SFBool outputOnly field named "isBound"
    def getIsBound(self):
        pass


