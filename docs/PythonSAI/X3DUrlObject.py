from . import *

class CX3DUrlObject(CX3DRootNode):
    m_strNodeName = "X3DurlObject"
    url = ""
    def __init__(self):
        self.m_strNodeName = "X3DUrlObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.url = ""

    def setURL(self, value):
        self.url = value

    def getURL(self):
        return self.url
