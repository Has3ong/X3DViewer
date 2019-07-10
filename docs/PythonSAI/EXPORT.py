from . import *

# EXPORT defines a concrete node interface that extends interface SceneGraphStructureStatement.
class CEXPORT(CSceneGraphStructureStatement):
    m_strNodeName = "EXPORT"
    def __init__(self):
        self.m_strNodeName = "EXPORT"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return xs:IDREF result [] from xs:IDREF type inputOutput field named "localDEF"
    def getLocalDEF (self):
        pass
      
    # Assign xs:IDREF value [] to xs:IDREF type inputOutput field named "localDEF"
    def setLocalDEF (self, value):
        pass
      
    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "AS"
    def getAS (self):
        pass
      
    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "AS"
    def setAS (self, value):
        pass
      