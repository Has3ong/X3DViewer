from . import *

class CGroup(CX3DGroupingNode):
    m_strNodeName = "Group"
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

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF