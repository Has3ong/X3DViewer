from . import *

class CX3DShapeNode(CX3DChildNode):
    m_strNodeName = "X3DShapeNode"

    geometry = CX3DGeometryNode()
    appearance = CAppearance()

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""

    def setGeometry(self, pNode):
        self.geometry = pNode
        pNode.m_Parent = self

    def setAppearance(self, pNode):
        self.appearance = pNode