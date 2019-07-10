from . import *


# SliderJoint defines a concrete node interface that extends interface X3DRigidJointNode.
# SliderJoint constrains all movement between body1 and body2 along a single axis. Contains two RigidBody nodes (containerField values body1, body2).

class CSliderJoint(CX3DRigidJointNode):
    m_strNodeName = "SliderJoint"
    def __init__(self):
        self.m_strNodeName = "SliderJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat outputOnly field named "separation"
    def getSeparation (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "separationRate"
    def getSeparationRate (self):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "axis"
    def getAxis (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "axis"
    def setAxis (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxSeparation"
    def getMaxSeparation (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxSeparation"
    def setMaxSeparation (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "minSeparation"
    def getMinSeparation (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "minSeparation"
    def setMinSeparation (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "sliderForce"
    def getSliderForce (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "sliderForce"
    def setSliderForce (self, value):
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
