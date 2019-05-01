from . import *

class CX3DShaderNode(CX3DAppearanceChildNode):
    m_strNodeName = "X3DShaderNode"
    def __init__(self):
        self.m_strNodeName = "X3DShaderNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass