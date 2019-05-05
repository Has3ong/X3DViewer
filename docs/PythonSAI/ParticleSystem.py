from . import *

class CParticleSystem(CX3DShapeNode):
    m_strNodeName = "ParticleSystem"
    def __init__(self):
        self.m_strNodeName = "ParticleSystem"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass