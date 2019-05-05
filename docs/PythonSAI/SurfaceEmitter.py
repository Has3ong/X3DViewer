from . import *

class CSurfaceEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "SurfaceEmitter"
    def __init__(self):
        self.m_strNodeName = "SurfaceEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass