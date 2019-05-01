from . import *

class CComposedTexture3D(CX3DTexture3DNode):
    m_strNodeName = "ComposedTexture3D"
    def __init__(self):
        self.m_strNodeName = "ComposedTexture3D"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass