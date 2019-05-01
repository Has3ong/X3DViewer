from . import *

class CRigidBody(CX3DNode):
    m_strNodeName = "RigidBody"
    def __init__(self):
        self.m_strNodeName = "RigidBody"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 

    pass