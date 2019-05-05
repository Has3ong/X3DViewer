from . import *

class CForcePhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "ForcePhysicsModel"
    def __init__(self):
        self.m_strNodeName = "ForcePhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass