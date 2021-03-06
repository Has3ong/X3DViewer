from . import *

# SingleAxisHingeJoint defines a concrete node interface that extends interface X3DRigidJointNode.
# SingleAxisHingeJoint has single axis about which to rotate, similar to a traditional door hinge. Contains two RigidBody nodes (containerField values body1, body2).

class CSingleAxisHingeJoint(CX3DRigidJointNode):
    m_strNodeName = "SingleAxisHingeJoint"
    def __init__(self):
        self.m_strNodeName = "SingleAxisHingeJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result in radians from SFFloat outputOnly field named "angle"
    def getAngle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "angleRate"
    def getAngleRate (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "body1AnchorPoint"
    def getBodyAnchorPoint (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "body2AnchorPoint"
    def getBody2AnchorPoint (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "anchorPoint"
    def getAnchorPoint (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "anchorPoint"
    def setAnchorPoint (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "axis"
    def getAxis (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "axis"
    def setAxis (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "maxAngle"
    def getMaxAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "maxAngle"
    def setMaxAngle (self, angle):
        pass

    # Return float result in radians from SFFloat inputOutput field named "minAngle"
    def getMinAngle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "minAngle"
    def setMinAngle (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "stopBounce"
    def getStopBounce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stopBounce"
    def setStopBounce (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stopErrorCorrection"
    def getStopErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stopErrorCorrection"
    def setStopErrorCorrection (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of String results array [] from MFString inputOutput field named "forceOutput"
    def getForceOutput (self):
        pass

    # Return number of primitive values in "forceOutput" array
    def getNumForceOutput (self):
        pass

    # Assign String array [] to MFString inputOutput field named "forceOutput"
    def setForceOutput1 (self, values):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "forceOutput"
    def setForceOutput2 (self, value):
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

    # Return RigidBody result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "body1"
    def getBody1 (self, result):
        pass

    # Assign RigidBody value (using a properly typed node) to SFNode inputOutput field named "body1"
    def setBody1 (self, node):
        pass

    # Assign RigidBody value (using a properly typed protoInstance)
    def setBody2 (self, protoInstance):
        pass

    # Return RigidBody result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "body2"
    def getBody2 (self, result):
        pass

    # Assign RigidBody value (using a properly typed node) to SFNode inputOutput field named "body2"
    def setBody3 (self, node):
        pass

    # Assign RigidBody value (using a properly typed protoInstance)
    def setBody4 (self, protoInstance):
        pass
