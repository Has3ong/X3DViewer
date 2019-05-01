from . import *

class CGroup(CX3DGroupingNode):
    m_strNodeName = "Group"

    def __init__(self, value = None):
        self.m_strNodeName = "Group"
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
        
    def Draw(self):
        print("not implment")

    #def toXMLString(self):

    #def getPropertyString(self):

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF