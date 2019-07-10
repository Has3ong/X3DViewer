from . import *

# head defines a concrete node interface that extends interface SceneGraphStructureStatement.
class CHead(CSceneGraphStructureStatement):
    m_strNodeName = "Head"
    def __init__(self):
        self.m_strNodeName = "Head"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    pass
