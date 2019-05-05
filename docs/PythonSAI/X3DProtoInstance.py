from . import *

class X3DProtoInstance(CX3DNode):
    m_strNodeName = "ProtoInstance"
    def __init__(self):
        self.m_strNodeName = "ProtoInstance"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass