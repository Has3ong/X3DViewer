from . import *

# RigidBody defines a concrete node interface that extends interface X3DNode.
class CRigidBody(CX3DNode):
    m_strNodeName = "RigidBody"
    def __init__(self):
        self.m_strNodeName = "RigidBody"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "angularDampingFactor"
    def getAngularDampingFactor (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "angularDampingFactor"
    def setAngularDampingFactor (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "angularVelocity"
    def getAngularVelocity (self, result):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "angularVelocity"
    def setAngularVelocity (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "autoDamp"
    def getAutoDamp (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "autoDamp"
    def setAutoDamp (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "autoDisable"
    def getAutoDisable (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "autoDisable"
    def setAutoDisable (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "centerOfMass"
    def getCenterOfMass (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "centerOfMass"
    def setCenterOfMass (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "disableAngularSpeed"
    def getDisableAngularSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "disableAngularSpeed"
    def setDisableAngularSpeed (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "disableLinearSpeed"
    def getDisableLinearSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "disableLinearSpeed"
    def setDisableLinearSpeed (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "disableTime"
    def getDisableTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "disableTime"
    def setDisableTime (self, timestamp):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return array of 3-tuple float results array in radians from SFVec3f inputOutput field named "finiteRotationAxis"
    def getFiniteRotationAxis (self):
        pass

    # Assign 3-tuple float array in radians to SFVec3f inputOutput field named "finiteRotationAxis"
    def setFiniteRotationAxis (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "fixed"
    def getFixed (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "fixed"
    def setFixed (self, value):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f inputOutput field named "forces"
    def getForces (self):
        pass

    # Return number of 3-tuple primitive values in "forces" array
    def getNumForces (self):
        pass

    # Assign 3-tuple float array [] to MFVec3f inputOutput field named "forces"
    def setForces (self, values):
        pass

    # Return array of float results array [] from SFMatrix3f inputOutput field named "inertia"
    def getInertia (self):
        pass

    # Assign float array [] to SFMatrix3f inputOutput field named "inertia"
    def setInertia (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "linearDampingFactor"
    def getLinearDampingFactor (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "linearDampingFactor"
    def setLinearDampingFactor (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "linearVelocity"
    def getLinearVelocity (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "linearVelocity"
    def setLinearVelocity (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "mass"
    def getMass (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "mass"
    def setMass (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "position"
    def getPosition (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "position"
    def setPosition (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "orientation"
    def getOrientation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "orientation"
    def setOrientation (self, value):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f inputOutput field named "torques"
    def getTorques (self):
        pass

    # Return number of 3-tuple primitive values in "torques" array
    def getNumTorques (self):
        pass

    # Assign 3-tuple float array [] to MFVec3f inputOutput field named "torques"
    def setTorques (self, values):
        pass

    # Return boolean result in radians from SFBool inputOutput field named "useFiniteRotation"
    def getUseFiniteRotation (self):
        pass

    # Assign boolean value in radians to SFBool inputOutput field named "useFiniteRotation"
    def setUseFiniteRotation (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "useGlobalGravity"
    def getUseGlobalGravity (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "useGlobalGravity"
    def setUseGlobalGravity (self, value):
        pass

    # Return array of X3DNBodyCollidableNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "geometry"
    def getGeometry (self, result):
        pass

    # Return number of nodes in "geometry" array
    def getNumGeometry (self):
        pass

    # Assign X3DNBodyCollidableNode array (using a properly typed node array) to MFNode inputOutput field named "geometry"
    def setGeometry1 (self, nodes):
        pass

    # Assign single X3DNBodyCollidableNode value (using a properly typed node) as the MFNode array for inputOutput field named "geometry"
    def setGeometry2 (self, node):
        pass

    # Assign X3DNBodyCollidableNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "geometry"
    def setGeometry3 (self, node):
        pass

    # Assign X3DNBodyCollidableNode array (using a properly typed node array) to MFNode inputOutput field named "geometry"
    def setGeometry4 (self, nodes):
        pass

    # Return Sphere|Box|Cone result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "massDensityModel"
    def getMassDensityModel (self, result):
        pass

    # Assign Sphere|Box|Cone value (using a properly typed node) to SFNode inputOutput field named "massDensityModel"
    def setMassDensityModel1 (self, node):
        pass

    # Assign Sphere|Box|Cone value (using a properly typed protoInstance)
    def setMassDensityModel2 (self, protoInstance):
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
