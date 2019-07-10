from . import *

# ProtoDeclare defines a concrete node interface that extends interface SceneGraphStructureStatement.
# ProtoDeclare defines new Prototype nodes. Nested ProtoDeclares, ProtoInstances are allowed by specification.
class CProtoDeclare(CSceneGraphStructureStatement):
    m_strNodeName = "ProtoDeclare"
    def __init__(self):
        self.m_strNodeName = "ProtoDeclare"
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
