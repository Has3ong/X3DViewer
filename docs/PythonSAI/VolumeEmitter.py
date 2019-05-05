from . import *

class CVolumeEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "CVolumeEmitter"
    def __init__(self):
        self.m_strNodeName = "CVolumeEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass