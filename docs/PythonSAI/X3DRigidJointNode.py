from . import *

class CX3DRigidJointNode(CX3DNode):
    m_strNodeName = "X3DRigidJointNode"
    def __init__(self):
        self.m_strNodeName = "X3DRigidJointNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass