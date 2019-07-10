from . import *

# ProtoInterface defines a concrete node interface that extends interface SceneGraphStructureStatement.
# ProtoInterface defines fields for new Prototype nodes.
class CProtoInterface(CSceneGraphStructureStatement):
    m_strNodeName = "ProtoInterface"
    def __init__(self):
        self.m_strNodeName = "ProtoInterface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
    pass