from . import *

# TouchSensor defines a concrete node interface that extends interface X3DTouchSensorNode.
class CTouchSensor(CX3DTouchSensorNode):
    m_strNodeName = "TouchSensor"
    def __init__(self):
        self.m_strNdeName = "TouchSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
        self.m_toNode = [None]
        self.m_tofield = [None]

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "hitNormal_changed"
    def getHitNormal (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "hitPoint_changed"
    def getHitPoint (self):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f outputOnly field named "hitTexCoord_changed"
    def getHitTexCoord (self):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool outputOnly field named "isOver"
    def getIsOver (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "touchTime"
    def getTouchTime (self):
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass


    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF

    def setSource(self, value):
        self.m_tofield[0] = value

    def setToNode(self, value):
        self.m_toNode[0] = value

    def getSource(self):
        return self.m_tofield[0]

    def getToNode(self):
        return self.m_toNode[0]

    def setField(self, value):
        self.m_tofield[0] = value