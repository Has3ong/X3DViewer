from . import *

# ROUTE defines a concrete node interface that extends interfaces SceneGraphStructureStatementX3DChildNode.
# ROUTE connects output fields of event-producing nodes to input fields of event-consuming nodes.
class CROUTE(CSceneGraphStructureStatement):
    m_strNodeName = "ROUTE"
    DEF = ""

    fromField = ""
    fromNode = ""
    toField = ""
    toNode = ""

    m_pSourceNode = []
    m_pDestinationNode = []

    def __init__(self):
        self.m_strNodeName = "ROUTE"
        self.fromField = ""
        self.fromNode = ""
        self.toField = ""
        self.toNode = ""
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.m_fromNode = []
        self.m_toNode = []

        self.m_Parent = [None]
        self.children = []

    def getDEF(self):
        return self.DEF

    def setDEF(self, value):
        self.DEF = value

    # Return xs:IDREF result [] from xs:IDREF type inputOutput field named "fromNode"
    def getFromNode(self):
        return self.fromNode

    # Assign xs:IDREF value [] to xs:IDREF type inputOutput field named "fromNode"
    def setFromNode(self, value):
        self.fromNode = value

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "fromField"
    def getFromField(self):
        return self.fromField

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "fromField"
    def setFromField(self, value):
        self.fromField = value

    # Return xs:IDREF result [] from xs:IDREF type inputOutput field named "toNode"
    def getToNode(self):
        return self.toNode

    # Assign xs:IDREF value [] to xs:IDREF type inputOutput field named "toNode"
    def setToNode(self, value):
        self.toNode = value

    # Return xs:NMTOKEN result [] from xs:NMTOKEN type inputOutput field named "toField"
    def getToField(self):
        return self.toField

    # Assign xs:NMTOKEN value [] to xs:NMTOKEN type inputOutput field named "toField"
    def setToField(self, value):
        self.toField = value

    def getSourceNode(self):
        return self.m_pSourceNode[0]

    def setSourceNode(self, value):
        self.m_pSourceNode[0] = value

    def getDestinationNode(self):
        return self.m_pDestinationNode[0]

    def setDestinationNode(self, value):
        self.m_pDestinationNode[0] = value
