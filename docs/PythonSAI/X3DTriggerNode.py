from . import *

class CX3DTriggerNode(CX3DChildNode):
    m_strNodeName = "X3DTriggerNode"
    def __init__(self):
        self.m_strNodeName = "X3DTriggerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass