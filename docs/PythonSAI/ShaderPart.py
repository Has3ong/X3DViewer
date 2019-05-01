from . import *

class CShaderPart(CX3DNode, CX3DUrlObject):
    m_strNodeName = "ShaderPart"
    def __init__(self):
        self.m_strNodeName = "ShaderPart"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 

    pass