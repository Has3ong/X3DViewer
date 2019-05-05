from . import *

class CWindPhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "WindPhysicsModel"
    def __init__(self):
        self.m_strNodeName = "WindPhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass