from . import *

#  X3DProgrammableShaderObject defines an abstract node interface.
class CX3DProgrammableShaderObject(CX3DNode):
    m_strNodeName = "X3DProgrammableShaderObject"
    def __init__(self):
        self.m_strNodeName = "X3DProgrammableShaderObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    pass