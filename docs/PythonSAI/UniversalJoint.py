from . import *

class CUniversalJoint(CX3DRigidJointNode):
    m_strNodeName = "UniversalJoint"
    def __init__(self):
        self.m_strNodeName = "UniversalJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass