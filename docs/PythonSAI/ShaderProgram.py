from . import *

class CShaderProgram(CX3DNode, CX3DUrlObject, CX3DProgrammableShaderObject):
    m_strNodeName = "ShaderProgram"
    def __init__(self):
        self.m_strNodeName = "ShaderProgram"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


    pass