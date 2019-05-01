from . import *

class CX3DShapeNode(CX3DChildNode):
    m_strNodeName = "X3DShapeNode"
    geometry = CX3DGeometryNode()
    appearance = CAppearance()
    def __init__(self):
        self.m_strNodeName = "X3DShapeNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.geometry = CX3DGeometryNode()
        self.appearance = self.CAppearance()
        

    def setGeometry(self, pNode):
        self.geometry = pNode
        pNode.m_Parent = self

    def setAppearance(self, pNode):
        self.appearance = pNode