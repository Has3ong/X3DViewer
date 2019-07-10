from . import *

# ProtoInstance defines a concrete node interface that extends interfaces X3DPrototypeInstanceX3DNode.
# Nested ProtoDeclares, ProtoInstances are allowed by specification. ProtoInstance contained content normally captured via fieldValue initializations.
class CProtoInstance(CSceneGraphStructureStatement):
    m_strNodeName = "ProtoInstance"
    def __init__(self):
        self.m_strNodeName = "ProtoInstance"
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