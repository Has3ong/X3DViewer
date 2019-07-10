from . import *

# IS defines a concrete node interface that extends interface SceneGraphStructureStatement.
class CIS(CX3DVolumeDataNode):
    m_strNodeName = "IS"
    def __init__(self):
        self.m_strNodeName = "IS"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
    pass