from . import *

class CScene(CSceneGraphStructureStatement):
    m_strNodeName = "Scene"
    def __init__(self):
        self.m_strNodeName = "Scene"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass
