from . import *

class CBoundedPhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "BoundedPhysicsModel"
    def __init__(self):
        self.m_strNodeName = "BoundedPhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass