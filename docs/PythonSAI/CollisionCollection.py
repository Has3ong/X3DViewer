from . import *

# CollisionCollection defines a concrete node interface that extends interface X3DNode.
class CCollisionCollection(CX3DNode):
    m_strNodeName = "CollisionCollection"
    def __init__(self):
        self.m_strNodeName = "CollisionCollection"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array array of appliedParameterValues. Note that strict validation of appliedParameters enumeration values does not occur via schema since MFString allows any value in any order. from MFString inputOutput field named "appliedParameters"
    def getAppliedParameters (self):
        pass

    # Return number of primitive values in "appliedParameters" array
    def getNumAppliedParameters (self):
        pass

    # Assign String array array of appliedParameterValues. Note that strict validation of appliedParameters enumeration values does not occur via schema since MFString allows any value in any order. to MFString inputOutput field named "appliedParameters"
    def setAppliedParameters1 (self, values):
        pass

    # Assign single String value array of appliedParameterValues. Note that strict validation of appliedParameters enumeration values does not occur via schema since MFString allows any value in any order. as the MFString array for inputOutput field named "appliedParameters"
    def setAppliedParameters2 (self, value):
        pass

    # Return float result [] from  type inputOutput field named "bounce"
    def getBounce (self):
        pass

    # Assign float value [] to  type inputOutput field named "bounce"
    def setBounce (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "frictionCoefficients"
    def getFrictionCoefficients (self, result):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "frictionCoefficients"
    def setFrictionCoefficients (self, value):
        pass

    # Return float result [] from  type inputOutput field named "minBounceSpeed"
    def getMinBounceSpeed (self):
        pass

    # Assign float value [] to  type inputOutput field named "minBounceSpeed"
    def setMinBounceSpeed (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "slipFactors"
    def getSlipFactors (self, result):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "slipFactors"
    def setSlipFactors (self, value):
        pass

    # Return float result [] from  type inputOutput field named "softnessConstantForceMix"
    def getSoftnessConstantForceMix (self):
        pass

    # Assign float value [] to  type inputOutput field named "softnessConstantForceMix"
    def setSoftnessConstantForceMix (self, value):
        pass

    # Return float result [] from  type inputOutput field named "softnessErrorCorrection"
    def getSoftnessErrorCorrection (self):
        pass

    # Assign float value [] to  type inputOutput field named "softnessErrorCorrection"
    def setSoftnessErrorCorrection (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "surfaceSpeed"
    def getSurfaceSpeed (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "surfaceSpeed"
    def setSurfaceSpeed (self, value):
        pass

    # Return array of X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "collidables"
    def getCollidables (self, result):
        pass

    # Return number of nodes in "collidables" array
    def getNumCollidables (self):
        pass

    # Assign X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode array (using a properly typed node array) to MFNode inputOutput field named "collidables"
    def setCollidables1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "collidables"
    def setCollidables2 (self, node):
        pass

    # Assign X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "collidables"
    def setCollidables3 (self, node):
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
