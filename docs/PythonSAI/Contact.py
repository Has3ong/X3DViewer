from . import *

# Contact defines a concrete node interface that extends interface X3DNode.
class CContact(CX3DNode):
    m_strNodeName = "Contact"
    def __init__(self):
        self.m_strNodeName = "Contact"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
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
    def setAppliedParameters (self, values, size):
        pass

    # Assign single String value array of appliedParameterValues. Note that strict validation of appliedParameters enumeration values does not occur via schema since MFString allows any value in any order. as the MFString array for inputOutput field named "appliedParameters"
    def setAppliedParameters (self, value):
        pass

    # Return float result [] from  type inputOutput field named "bounce"
    def getBounce (self):
        pass

    # Assign float value [] to  type inputOutput field named "bounce"
    def setBounce (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "contactNormal"
    def getContactNormal (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "contactNormal"
    def setContactNormal (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "depth"
    def getDepth (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "depth"
    def setDepth (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "frictionCoefficients"
    def getFrictionCoefficients (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "frictionCoefficients"
    def setFrictionCoefficients (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "frictionDirection"
    def getFrictionDirection (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "frictionDirection"
    def setFrictionDirection (self, value):
        pass

    # Return float result [] from  type inputOutput field named "minBounceSpeed"
    def getMinBounceSpeed (self):
        pass

    # Assign float value [] to  type inputOutput field named "minBounceSpeed"
    def setMinBounceSpeed (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "position"
    def getPosition (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "position"
    def setPosition (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "slipCoefficients"
    def getSlipCoefficients (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "slipCoefficients"
    def setSlipCoefficients (self, value):
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

    # Return RigidBody result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "body1"
    def getBody1 (self, result):
        pass

    # Assign RigidBody value (using a properly typed node) to SFNode inputOutput field named "body1"
    def setBody1 (self, node):
        pass

    # Assign RigidBody value (using a properly typed protoInstance)
    def setBody1 (self, protoInstance):
        pass

    # Return RigidBody result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "body2"
    def getBody2 (self, result):
        pass

    # Assign RigidBody value (using a properly typed node) to SFNode inputOutput field named "body2"
    def setBody2 (self, node):
        pass

    # Assign RigidBody value (using a properly typed protoInstance)
    def setBody2 (self, protoInstance):
        pass

    # Return X3DNBodyCollidableNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "geometry1"
    def getGeometry1 (self, result):
        pass

    # Assign X3DNBodyCollidableNode value (using a properly typed node) to SFNode inputOutput field named "geometry1"
    def setGeometry1 (self, node):
        pass

    # Assign X3DNBodyCollidableNode value (using a properly typed protoInstance)
    def setGeometry2 (self, protoInstance):
        pass

    # Return X3DNBodyCollidableNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "geometry2"
    def getGeometry2 (self, result):
        pass

    # Assign X3DNBodyCollidableNode value (using a properly typed node) to SFNode inputOutput field named "geometry2"
    def setGeometry3 (self, node):
        pass

    # Assign X3DNBodyCollidableNode value (using a properly typed protoInstance)
    def setGeometry4 (self, protoInstance):
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
