from . import *

class CPointEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "PointEmitter"
    def __init__(self):
        self.m_strNodeName = "PointEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass