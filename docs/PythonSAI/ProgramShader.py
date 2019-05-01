from . import *

class CProgramShader(CX3DShaderNode,):
    m_strNodeName = "ProgramShader"

    def __init__(self):
        self.m_strNodeName = "ProgramShader"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


    pass