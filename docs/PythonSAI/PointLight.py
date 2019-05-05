from . import *

class CPointLight(CX3DLightNode):
    m_strNodeName = "PointLight"
    def __init__(self):
        self.m_strNodeName = "PointLight"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass