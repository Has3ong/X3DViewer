from . import *

# connect defines a concrete node interface that extends interface SceneGraphStructureStatement.
class Cconnect(CSceneGraphStructureStatement):
    m_strNodeName = "connect"
    def __init__(self):
        self.m_strNodeName = "connect"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "nodeField"
    def getNodeField (self):
        pass

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "nodeField"
    def setNodeField (self, value):
        pass

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "protoField"
    def getProtoField (self):
        pass

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "protoField"
    def setProtoField (self, value):
        pass
