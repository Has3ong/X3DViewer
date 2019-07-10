from . import *

# MotorJoint defines a concrete node interface that extends interface X3DRigidJointNode.
class CMotorJoint(CX3DRigidJointNode):
    m_strNodeName = "MotorJoint"
    def __init__(self):
        self.m_strNodeName = "MotorJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result in radians from SFFloat outputOnly field named "motor1Angle"
    def getMotor1Angle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "motor1AngleRate"
    def getMotor1AngleRate (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "motor2Angle"
    def getMotor2Angle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "motor2AngleRate"
    def getMotor2AngleRate (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "motor3Angle"
    def getMotor3Angle (self):
        pass

    # Return float result in radians from SFFloat outputOnly field named "motor3AngleRate"
    def getMotor3AngleRate (self):
        pass

    # Return boolean result from SFBool initializeOnly field named "autoCalc"
    def getAutoCalc (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "autoCalc"
    def setAutoCalc (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "axis1Angle"
    def getAxis1Angle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "axis1Angle"
    def setAxis1Angle (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "axis1Torque"
    def getAxis1Torque (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "axis1Torque"
    def setAxis1Torque (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "axis2Angle"
    def getAxis2Angle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "axis2Angle"
    def setAxis2Angle (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "axis2Torque"
    def getAxis2Torque (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "axis2Torque"
    def setAxis2Torque (self, value):
        pass

    # Return float result in radians from SFFloat inputOutput field named "axis3Angle"
    def getAxis3Angle (self):
        pass

    # Assign float value in radians to SFFloat inputOutput field named "axis3Angle"
    def setAxis3Angle (self, angle):
        pass

    # Return float result [] from SFFloat inputOutput field named "axis3Torque"
    def getAxis3Torque (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "axis3Torque"
    def setAxis3Torque (self, value):
        pass

    # Return int result [] from  type inputOutput field named "enabledAxes"
    def getEnabledAxes (self):
        pass

    # Assign int value [] to  type inputOutput field named "enabledAxes"
    def setEnabledAxes (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "motor1Axis"
    def getMotor1Axis (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "motor1Axis"
    def setMotor1Axis (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "motor2Axis"
    def getMotor2Axis (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "motor2Axis"
    def setMotor2Axis (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "motor3Axis"
    def getMotor3Axis (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "motor3Axis"
    def setMotor3Axis (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop1Bounce"
    def getStop1Bounce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop1Bounce"
    def setStop1Bounce (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop1ErrorCorrection"
    def getStop1ErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop1ErrorCorrection"
    def setStop1ErrorCorrection (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop2Bounce"
    def getStop2Bounce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop2Bounce"
    def setStop2Bounce (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop2ErrorCorrection"
    def getStop2ErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop2ErrorCorrection"
    def setStop2ErrorCorrection (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop3Bounce"
    def getStop3Bounce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop3Bounce"
    def setStop3Bounce (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "stop3ErrorCorrection"
    def getStop3ErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "stop3ErrorCorrection"
    def setStop3ErrorCorrection (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of String results array [] from MFString inputOutput field named "forceOutput"
    def getForceOutput (self):
        pass

    # Return number of primitive values in "forceOutput" array
    def getNumForceOutput (self):
        pass

    # Assign String array [] to MFString inputOutput field named "forceOutput"
    def setForceOutput1 (self, values, size):
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
