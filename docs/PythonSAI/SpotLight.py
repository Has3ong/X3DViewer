from . import *

class CSpotLight(CX3DLightNode):
    m_strNodeName = "SpotLight"
    def __init__(self):
        self.m_strNodeName = "SpotLight"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass