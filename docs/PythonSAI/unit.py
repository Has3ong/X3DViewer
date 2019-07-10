from . import *

# unit defines a concrete node interface that extends interface SceneGraphStructureStatement.
class Cunit(CSceneGraphStructureStatement):
    m_strNodeName = "unit"
    def __init__(self):
        self.m_strNodeName = "unit"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    # Return String enumeration result ("angle"|"force"|"length"|"mass") from unitCategories type initializeOnly field named "category"
    def getCategory (self):
        pass

    # Assign String enumeration value ("angle"|"force"|"length"|"mass") to unitCategories type initializeOnly field named "category"
    def setCategory (self, value):
        pass

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "name"
    def getName (self):
        pass

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return double result [] from  type inputOutput field named "conversionFactor"
    def getConversionFactor (self):
        pass

    # Assign double value [] to  type inputOutput field named "conversionFactor"
    def setConversionFactor (self, value):
        pass