from . import *

class CX3DShapeNode(CX3DChildNode):
    m_strNodeName = "X3DShapeNode"

    geometry = CX3DGeometryNode()
    appearance = CAppearance()

    def setGeometry(self, pNode):
        self.geometry = pNode
        pNode.m_Parent = self

    def setAppearance(self, pNode):
        self.appearance = pNode