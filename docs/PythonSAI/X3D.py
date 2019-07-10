from . import *

# WorldInfo defines a concrete node interface that extends interface X3DInfoNode
class CX3D(CSceneGraphStructureStatement):
    m_strNodeName = "X3D"
    def __init__(self):
        self.m_strNodeName = "X3D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from x3dVersion type inputOutput field named "version"
    def getVersion (self):
        pass

    # Assign String value [] to x3dVersion type inputOutput field named "version"
    def setVersion (self, value):
        pass

    # Return String result [] from profileNames type inputOutput field named "profile"
    def getProfile (self):
        pass

    # Assign String value [] to profileNames type inputOutput field named "profile"
    def setProfile (self, value):
        pass
