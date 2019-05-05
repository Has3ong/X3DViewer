from . import *

class CBallJoint(CX3DRigidJointNode):
    m_strNodeName = "BallJoint"
    def __init__(self):
        self.m_strNodeName = "BallJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass