from . import *

class CSingleAxisHingeJoint(CX3DRigidJointNode):
    m_strNodeName = "SingleAxisHingeJoint"
    def __init__(self):
        self.m_strNodeName = "SingleAxisHingeJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass