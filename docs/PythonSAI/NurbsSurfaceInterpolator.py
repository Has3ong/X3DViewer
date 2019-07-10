from . import *

# NurbsSurfaceInterpolator defines a concrete node interface that extends interface X3DChildNode.
class CNurbsSurfaceInterpolator(CX3DChildNode):
    m_strNodeName = "NurbsSurfaceInterpolator"
    def __init__(self):
        self.m_strNodeName = "NurbsSurfaceInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign 2-tuple float array [] to SFVec2f inputOnly field named "set_fraction"
    def setFraction (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "position_changed"
    def getPosition (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "normal_changed"
    def getNormal (self, result):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "uDimension"
    def getUDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "uDimension"
    def setUDimension (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "vDimension"
    def getVDimension (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "vDimension"
    def setVDimension (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "uKnot"
    def getUKnot (self):
        pass

    # Return number of primitive values in "uKnot" array
    def getNumUKnot (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "uKnot"
    def setUKnot1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "uKnot"
    def setUKnot2 (self, value):
        pass

    # Return array of double results array [] from MFDouble initializeOnly field named "vKnot"
    def getVKnot (self):
        pass

    # Return number of primitive values in "vKnot" array
    def getNumVKnot (self):
        pass

    # Assign double array [] to MFDouble initializeOnly field named "vKnot"
    def setVKnot1 (self, values, size):
        pass

    # Assign single double value [] as the MFDouble array for initializeOnly field named "vKnot"
    def setVKnot2 (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "uOrder"
    def getUOrder (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "uOrder"
    def setUOrder (self, value):
        pass

    # Return int result [] from SFInt32 initializeOnly field named "vOrder"
    def getVOrder (self):
        pass

    # Assign int value [] to SFInt32 initializeOnly field named "vOrder"
    def setVOrder (self, value):
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
    def setWeigh2t (self, value):
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
