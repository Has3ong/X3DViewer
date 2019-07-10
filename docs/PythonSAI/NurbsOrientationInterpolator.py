from . import *

# NurbsOrientationInterpolator defines a concrete node interface that extends interface X3DChildNode.
class CNurbsOrientationInterpolator(CX3DChildNode):
    m_strNodeName = "NurbsOrientationInterpolator"
    def __init__(self):
        self.m_strNodeName = "NurbsOrientationInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign float value [] to SFFloat inputOnly field named "set_fraction"
    def setFraction (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation outputOnly field named "value_changed"
    def getValue (self):
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

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "controlPoint"
    def getControlPoint (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "controlPoint"
    def setControlPoint1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setControlPoint2 (self, protoInstance):
        pass

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
