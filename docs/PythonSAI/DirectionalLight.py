from . import *

class CDirectionalLight(CX3DLightNode):
    m_strNodeName = "DirectionalLight"
    def __init__(self):
        self.m_strNodeName = "DirectionalLight"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass