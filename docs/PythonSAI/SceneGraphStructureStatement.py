from . import *

class CSceneGraphStructureStatement(CX3DRootNode):
    m_strNodeName = "SceneGraphStructureStatement"
    def __init__(self):
        self.m_strNodeName = "SceneGraphStructureStatement"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass