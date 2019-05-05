from . import *

class CExplosionEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "ExplosionEmitter"
    def __init__(self):
        self.m_strNodeName = "ExplosionEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass