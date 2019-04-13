from X3DLib import *

class CShape(CX3DShapeNode):
    m_strNodeName = "Shape"
    DEF = ""

    def __init__(self, value = None):
        if value == None:
            self.DEF = ""
            self.m_Parent = [None]
            self.children = []
            
        self.DEF = ""
        self.m_Parent = [None]
        self.children = []


    def Draw(self):
        print("not implment")

    #def toXMLString(self):

    #def getPropertyString(self):

    def setGeometry(self, node):
        self.addChildren(node)

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF