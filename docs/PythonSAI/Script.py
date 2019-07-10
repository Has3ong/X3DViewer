from . import *

# Script defines a concrete node interface that extends interface X3DScriptNode.
class CScript(CX3DScriptNode):
    m_strNodeName = "Script"
    directOutput = False
    mustEvaluate = False
    def __init__(self):
        self.m_strNodeName = "Script"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.url = ""
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
        self.directOutput = False
        self.mustEvaluate = False

        self.m_tofield = [None]
        self.m_toNode = [None]

    # Return boolean result from SFBool initializeOnly field named "directOutput"
    def getDirectOutput(self):
        return self.directOutput

    # Assign boolean value to SFBool initializeOnly field named "directOutput"
    def setDirectOutput(self, value):
        self.directOutput = value

    # Return boolean result from SFBool initializeOnly field named "mustEvaluate"
    def getMustEvaluate(self):
        return self.mustEvaluate

    # Assign boolean value to SFBool initializeOnly field named "mustEvaluate"
    def setMustEvaluate(self, value):
        self.mustEvaluate = value

    def setDiffuseColor(self, value):
        mat = self.m_toNode[0]
        mat.setDiffuseColor2(value)

    def setSource(self, value):
        self.m_tofield[0] = value

    def getSource(self):
        return self.m_tofield[0]

    def setToNode(self, value):
        self.m_toNode[0] = value

    def getToNode(self):
        return self.m_toNode[0]

    def setField(self, value):
        self.m_tofield[0] = value

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass


    