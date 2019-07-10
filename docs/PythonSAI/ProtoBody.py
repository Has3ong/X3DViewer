from . import *

# ProtoBody defines a concrete node interface that extends interface SceneGraphStructureStatement.
# ProtoBody contains the definition nodes for new Prototype nodes.

class CProtoBody(CSceneGraphStructureStatement):
    m_strNodeName = "ProtoBody"
    def __init__(self):
        self.m_strNodeName = "ProtoBody"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
    pass