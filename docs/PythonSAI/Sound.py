from . import *

# Sound defines a concrete node interface that extends interface X3DSoundNode.
class CSound(CX3DSoundNode):
    m_strNodeName = "Sound"
    def __init__(self):
        self.m_strNodeName = "Sound"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "direction"
    def getDirection (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "direction"
    def setDirection (self, value):
        pass

    # Return float result [] from intensityType type inputOutput field named "intensity"
    def getIntensity (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "intensity"
    def setIntensity (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "location"
    def getLocation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "location"
    def setLocation (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxBack"
    def getMaxBack (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxBack"
    def setMaxBack (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxFront"
    def getMaxFront (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxFront"
    def setMaxFront (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "minBack"
    def getMinBack (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "minBack"
    def setMinBack (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "minFront"
    def getMinFront (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "minFront"
    def setMinFront (self, value):
        pass

    # Return float result [] from intensityType type inputOutput field named "priority"
    def getPriority (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "priority"
    def setPriority (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "spatialize"
    def getSpatialize (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "spatialize"
    def setSpatialize (self, value):
        pass

    # Return X3DSoundSourceNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "source"
    def getSource (self, result):
        pass

    # Assign X3DSoundSourceNode value (using a properly typed node) to SFNode inputOutput field named "source"
    def setSource1 (self, node):
        pass

    # Assign X3DSoundSourceNode value (using a properly typed protoInstance)
    def setSource2 (self, protoInstance):
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
