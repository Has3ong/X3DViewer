from . import *

class CComposedShader(CX3DShaderNode, CX3DProgrammableShaderObject):
    m_strNodeName = "ComposedShader"
    def __init__(self):
        self.m_strNodeName = "ComposedShader"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 

    pass