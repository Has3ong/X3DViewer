from . import *

class CX3DViewpointNode(CX3DBindableNode):
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

        self.jump = True
        self.retainUserOffsets = False
        self.position = [0.0, 0.0, 10.0]
        self.orientation = [0.0, 0.0, 1.0, 0.0]
        self.centerOfRotation = [0.0, 0.0, 0.0]
    def setDescription(self, value):
        self.description = value

    def getDescription(self):
        return self.description

    def setJump(self, value):
        self.jump = value

    def getJump(self):
        return self.jump

    def getOrientation(self):
        return None
    
    def setRetainUserOffsets(self, value):
        self.retainUserOffsets = value

    def getRetainUserOffsets(self):
        return self.retainUserOffsets

    def setBind(self, value):
        return None

    def getBindTime(self):
        return 0

    def getIsBound(self):
        return True

    def setPosition(self, pos):
        self.position[0] = pos.x()
        self.position[1] = pos.y()
        self.position[2] = pos.z()

    def setOrientation(self, ori):
        self.orientation[0] = ori.x()
        self.orientation[1] = ori.y()
        self.orientation[2] = ori.z()
        self.orientation[3] = ori.w()

    def setCenterOfRotation(self, cen):
        self.centerOfRotation[0] = cen.x()
        self.centerOfRotation[1] = cen.y()
        self.centerOfRotation[2] = cen.z()

    def getPosition(self):
        ret = CSFVec3f()
        ret.setValue3(self.position[0], self.position[1], self.position[2])

        return ret

    def getOrientation(self):
        ret = CSFRotation()
        ret.setValue4(self.orientation[0], self.orientation[1], self.orientation[2], self.orientation[3])

        return ret

    def getCenterOfRotation(self):
        ret = CSFVec3f()
        ret.setValue3(self.centerOfRotation[0], self.centerOfRotation[1], self.centerOfROtation[2])

        return ret
