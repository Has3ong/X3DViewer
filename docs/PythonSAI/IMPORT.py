from . import *

# IMPORT defines a concrete node interface that extends interface SceneGraphStructureStatement.
class CIMPORT(CSceneGraphStructureStatement):
    m_strNodeName = "IMPORT"
    def __init__(self):
        self.m_strNodeName = "IMPORT"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return xs:IDREF result [] from xs:IDREF type inputOutput field named "inlineDEF"
    def getInlineDEF (self):
        pass

    # Assign xs:IDREF value [] to xs:IDREF type inputOutput field named "inlineDEF"
    def setInlineDEF (self, value):
        pass

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "importedDEF"
    def getImportedDEF (self):
        pass

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "importedDEF"
    def setImportedDEF (self, value):
        pass

    # Return xs:ID result [] from xs:ID type inputOutput field named "AS"
    def getAS (self):
        pass

    # Assign xs:ID value [] to xs:ID type inputOutput field named "AS"
    def setAS (self, value):
        pass
