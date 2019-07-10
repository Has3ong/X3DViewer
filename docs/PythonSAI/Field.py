from . import *

# field defines a concrete node interface that extends interface SceneGraphStructureStatement.
# field can contain either attribute-value or node content. field is utilized by ExternProtoDeclare, ProtoDeclare and Script nodes.
class CField(CSceneGraphStructureStatement):
    m_strNodeName = "Field"
    name = ""
    accessType = ""
    m_type = ""
    value = ""
    appinfo = ""
    documentation = ""
    field = ""

    def __init__(self):
        self.m_strNodeName = "Field"
        self.name = ""
        self.accessType = ""
        self.m_type = ""
        self.value = ""
        self.appinfo = ""
        self.documentation = ""
        self.field = ""
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "name"
    def getName(self):
        return self.name

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "name"
    def setName(self, value):
        self.name = value

    # Return String result [] from accessTypeNames type inputOutput field named "accessType"
    def getAccessType(self):
        return self.accessType

    # Assign String value [] to accessTypeNames type inputOutput field named "accessType"
    def setAccessType(self, value):
        self.accessType = value

    # Return String result [] from fieldTypeName type inputOutput field named "type"
    def getType(self):
        return self.m_type

    # Assign String value [] to fieldTypeName type inputOutput field named "type"
    def setType(self, value):
        self.m_type = value

    # Return String result [] from SFString inputOutput field named "value"
    def getValue(self):
        return self.value

    # Assign String value [] to SFString inputOutput field named "value"
    def setValue(self, val):
        self.value = val

    # Return String result [] from SFString inputOutput field named "appinfo"
    def getAppInfo(self):
        return self.appinfo

    # Assign String value [] to SFString inputOutput field named "appinfo"
    def setAppInfo(self, value):
        self.appinfo = value

    # Return String result [] from SFString inputOutput field named "documentation"
    def getDocumentation(self):
        return self.documentation

    # Assign String value [] to SFString inputOutput field named "documentation"
    def setDocumentation(self, value):
        self.documentation = value

    def getField(self):
        return self.field

    def setField(self, value):
        self.field = value
