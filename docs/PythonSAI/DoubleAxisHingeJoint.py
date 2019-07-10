from . import *

# DoubleAxisHingeJoint defines a concrete node interface that extends interface X3DRigidJointNode.
class CDoubleAxisHingeJoint(CX3DRigidJointNode):
    m_strNodeName = "DoubleAxisHingeJoint"
    def __init__(self):
        self.m_strNodeName = "DoubleAxisHingeJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "body1AnchorPoint"
    def getBodyAnchorPoint (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "body1Axis"
    def getBody1Axis (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f outputOnly field named "body2AnchorPoint"
    def getBodyAnchorPoint (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "body2Axis"
    def getBody2Axis (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "hinge1Angle"
    def getHinge1Angle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "hinge1AngleRate"
    def getHinge1AngleRate (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "hinge2Angle"
    def getHinge2Angle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "hinge2AngleRate"
    def getHinge2AngleRate (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "anchorPoint"
    def getAnchorPoint (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "anchorPoint"
    def setAnchorPoint (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "axis1"
    def getAxis1 (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "axis1"
    def setAxis1 (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "axis2"
    def getAxis2 (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "axis2"
    def setAxis2 (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "desiredAngularVelocity1"
    def getDesiredAngularVelocity1 (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "desiredAngularVelocity1"
    def setDesiredAngularVelocity1 (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "desiredAngularVelocity2"
    def getDesiredAngularVelocity2 (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "desiredAngularVelocity2"
    def setDesiredAngularVelocity2 (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "maxAngle1"
    def getMaxAngle1 (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "maxAngle1"
    def setMaxAngle1 (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxTorque1"
    def getMaxTorque1 (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxTorque1"
    def setMaxTorque1 (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxTorque2"
    def getMaxTorque2 (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxTorque2"
    def setMaxTorque2 (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "minAngle1"
    def getMinAngle1 (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "minAngle1"
    def setMinAngle1 (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop1Bounce"
    def getStop1Bounce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop1Bounce"
    def setStop1Bounce (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop1ConstantForceMix"
    def getStop1ConstantForceMix (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop1ConstantForceMix"
    def setStop1ConstantForceMix (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop1ErrorCorrection"
    def getStop1ErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop1ErrorCorrection"
    def setStop1ErrorCorrection (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "suspensionErrorCorrection"
    def getSuspensionErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "suspensionErrorCorrection"
    def setSuspensionErrorCorrection (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "suspensionForce"
    def getSuspensionForce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "suspensionForce"
    def setSuspensionForce (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of String results array [] from MFString inputOutput field named "forceOutput"
    def getForceOutput (self):
        pass

    # Return number of primitive values in "forceOutput" array
    def getNumForceOutput (self):
        pass

    # Assign String array [] to MFString inputOutput field named "forceOutput"
    def setForceOutput (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "forceOutput"
    def setForceOutput (self, value):
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
