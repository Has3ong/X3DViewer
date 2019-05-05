from . import *

class CConeEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "ConeEmitter"
    def __init__(self):
        self.m_strNodeName = "ConeEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass