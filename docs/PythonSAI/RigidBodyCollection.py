from . import *

class CRigidBodyCollection(CX3DChildNode):
    m_strNodeName = "RigidBodyCollection"
    def __init__(self):
        self.m_strNodeName = "RigidBodyCollection"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass