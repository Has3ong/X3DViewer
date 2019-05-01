from . import *

class CShape(CX3DShapeNode):
    m_strNodeName = "Shape"
    def __init__(self, value = None):
        self.m_strNodeName = "Shape"
        if value == None:
            self.m_Parent = [None]
            self.children = []
            self.DEF = ""
            self.USE = ""
            self.n_Count = -1
        else:
            self.m_Parent = [None]
            self.children = []
            self.DEF = ""
            self.USE = ""
            self.n_Count = -1

    def setGeometry(self, node):
        self.addChildren(node)

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF