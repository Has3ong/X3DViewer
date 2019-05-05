from . import *

class CPolylineEmitter(CX3DParticleEmitterNode):
    m_strNodeName = "PolylineEmitter"
    def __init__(self):
        self.m_strNodeName = "PolylineEmitter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass