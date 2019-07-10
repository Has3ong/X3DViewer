from . import *

# NurbsTextureCoordinate defines a concrete node interface that extends interface X3DNode.
class CNurbsTextureCoordinate(CX3DNode):
    m_strNodeName = "NurbsTextureCoordinate"
    def __init__(self):
        self.m_strNodeName = "NurbsTextureCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 2-tuple float results array [] from MFVec2f inputOutput field named "controlPoint"
    def getControlPoint (self, result):
        pass

    # Return number of 2-tuple primitive values in "controlPoint" array
    def getNumControlPoint (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOutput field named "controlPoint"
    def setControlPoint (self, values, size):
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
    def setUKnot1 (self, values):
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

    # Return array of float results array [] from MFFloat inputOutput field named "weight"
    def getWeight (self):
        pass

    # Return number of primitive values in "weight" array
    def getNumWeight (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "weight"
    def setWeight (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "weight"
    def setWeight (self, value):
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
