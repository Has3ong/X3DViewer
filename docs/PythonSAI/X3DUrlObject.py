from . import *
# X3DUrlObject defines an abstract node interfac
# X3DUrlObject indicates that a node has content loaded from a URL and can be tracked via a LoadSensor.

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
        self.depth = 0

        self.url = ""

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getURL(self):
        return self.url

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2 (self, value):
        pass

    def setURL(self, value):
        self.url = value




