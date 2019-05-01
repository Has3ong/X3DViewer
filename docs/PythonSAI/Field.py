from . import *

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
 

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name

    def setAccessType(self, value):
        self.accessType = value

    def getAccessType(self):
        return self.accessType

    def setType(self, value):
        self.m_type = value

    def getType(self):
        return self.m_type

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value

    def setAppInfo(self, value):
        self.appinfo = value
    
    def getAppInfo(self):
        return self.appinfo

    def setDocumentation(self, value):
        self.documentation = value

    def getDocumentation(self):
        return self.documentation

    def setField(self, value):
        self.field = value

    def getField(self):
        return self.field

    

    