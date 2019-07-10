from . import *

# fieldValue defines a concrete node interface that extends interface SceneGraphStructureStatement.
# fieldValue can contain either attribute-value or node content. fieldValue is utilized by ProtoInstance nodes, reinitializing default values specified in ProtoDeclare field elements.
class CfieldValue(CSceneGraphStructureStatement):
    m_strNodeName = "fieldValue"
    def __init__(self):
        self.m_strNodeName = "fieldValue"
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

    # Return String result [] from SFString inputOutput field named "value"
    def getValue (self):
        pass

    # Assign String value [] to SFString inputOutput field named "value"
    def setValue (self, value):
        pass
