from . import *

# NurbsCurve2D defines a concrete node interface that extends interface X3DNurbsControlCurveNode.
class CNurbsCurve2D(CX3DNurbsControlCurveNode):
    m_strNodeName = "NurbsCurve2D"
    def __init__(self):
        self.m_strNodeName = "NurbsCurve2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool initializeOnly field named "closed"
    def getClosed (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "closed"
    def setClosed (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "knot"
    def getKnot (self):
        pass

    # Return number of primitive values in "knot" array
    def getNumKnot (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "knot"
    def setKnot1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "knot"
    def setKnot2 (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "order"
    def getOrder (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "order"
    def setOrder (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "tessellation"
    def getTessellation (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "tessellation"
    def setTessellation (self, value):
        pass

    # Return array of double results array [] from MFDouble inputOutput field named "weight"
    def getWeight (self):
        pass

    # Return number of primitive values in "weight" array
    def getNumWeight (self):
        pass

    # Assign double array [] to MFDouble inputOutput field named "weight"
    def setWeight1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for inputOutput field named "weight"
    def setWeight2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 2-tuple double results array [] from MFVec2d inputOutput field named "controlPoint"
    def getControlPoint (self):
        pass

    # Return number of 2-tuple primitive values in "controlPoint" array
    def getNumControlPoint (self):
        pass

    # Assign 2-tuple double array [] to MFVec2d inputOutput field named "controlPoint"
    def setControlPoint (self, values, size):
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
