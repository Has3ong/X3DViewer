from . import *

class CMotorJoint(CX3DRigidJointNode):
    m_strNodeName = "MotorJoint"
    def __init__(self):
        self.m_strNodeName = "MotorJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass