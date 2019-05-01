from . import *

class CPackagedShader(CX3DShaderNode, CX3DUrlObject, CX3DProgrammableShaderObject):
    m_strNodeName = "PackagedShader"
    def __init__(self):
        self.m_strNodeName = "PackagedShader"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


    pass