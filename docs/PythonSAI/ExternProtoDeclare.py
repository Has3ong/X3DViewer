from . import *

# ExternProtoDeclare defines a concrete node interface that extends interface SceneGraphStructureStatement.
# ExternProtoDeclare refers to a ProtoDeclare node declaration provided in another file. ExternProtoDeclare interfaces are defined with field elements (without IS attributes).
class CExternProtoDeclare(CSceneGraphStructureStatement):
    m_strNodeName = "ExternProtoDeclare"
    def __init__(self):
        self.m_strNodeName = "ExternProtoDeclare"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "name"
    def getName (self):
        pass

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getUrl (self):
        pass

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2 (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "appinfo"
    def getAppinfo (self):
        pass

    # Assign String value [] to SFString inputOutput field named "appinfo"
    def setAppinfo (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "documentation"
    def getDocumentation (self):
        pass

    # Assign String value [] to SFString inputOutput field named "documentation"
    def setDocumentation (self, value):
        pass
     