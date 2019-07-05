from . import *

# component defines a concrete node interface that extends interface SceneGraphStructureStatement.
class Ccomponent(CSceneGraphStructureStatement):
    m_strNodeName = "component"
    def __init__(self):
        self.m_strNodeName = "component"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from componentNames type inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to componentNames type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return int result [] from  type inputOutput field named "level"
    def getLevel (self):
        pass

    # Assign int value [] to  type inputOutput field named "level"
    def setLevel (self, value):
        pass
