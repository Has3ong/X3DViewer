from . import *

# RigidBodyCollection defines a concrete node interface that extends interface X3DChildNode.
class CRigidBodyCollection(CX3DChildNode):
    m_strNodeName = "RigidBodyCollection"
    def __init__(self):
        self.m_strNodeName = "RigidBodyCollection"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "autoDisable"
    def getAutoDisable (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "autoDisable"
    def setAutoDisable (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "constantForceMix"
    def getConstantForceMix (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "constantForceMix"
    def setConstantForceMix (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "contactSurfaceThickness"
    def getContactSurfaceThickness (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "contactSurfaceThickness"
    def setContactSurfaceThickness (self, value):
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

    # Return float result [] from SFFloat inputOutput field named "errorCorrection"
    def getErrorCorrection (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "errorCorrection"
    def setErrorCorrection (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "gravity"
    def getGravity (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "gravity"
    def setGravity (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "iterations"
    def getIterations (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "iterations"
    def setIterations (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "maxCorrectionSpeed"
    def getMaxCorrectionSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "maxCorrectionSpeed"
    def setMaxCorrectionSpeed (self,value):
        pass

    # Return boolean result from SFBool inputOutput field named "preferAccuracy"
    def getPreferAccuracy (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "preferAccuracy"
    def setPreferAccuracy (self, value):
        pass

    # Assign Contact array (using a properly typed node array) to MFNode inputOnly field named "set_contacts"
    def setContacts1 (self, nodes):
        pass

    # Assign single Contact value (using a properly typed node) as the MFNode array for inputOnly field named "set_contacts"
    def setContacts2 (self, node):
        pass

    # Assign Contact array (using a properly typed protoInstance array) to MFNode inputOnly field named "set_contacts"
    def setContacts3 (self, node):
        pass

    # Assign Contact array (using a properly typed node array) to MFNode inputOnly field named "set_contacts"
    def setContacts4 (self, nodes):
        pass

    # Return array of RigidBody results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "bodies"
    def getBodies (self, result):
        pass

    # Return number of nodes in "bodies" array
    def getNumBodies (self):
        pass

    # Assign RigidBody array (using a properly typed node array) to MFNode inputOutput field named "bodies"
    def setBodies1 (self, nodes):
        pass

    # Assign single RigidBody value (using a properly typed node) as the MFNode array for inputOutput field named "bodies"
    def setBodies2 (self, node):
        pass

    # Assign RigidBody array (using a properly typed protoInstance array) to MFNode inputOutput field named "bodies"
    def setBodies3 (self, node):
        pass

    # Assign RigidBody array (using a properly typed node array) to MFNode inputOutput field named "bodies"
    def setBodies4 (self, nodes):
        pass

    # Return array of X3DRigidJointNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "joints"
    def getJoints (self, result):
        pass

    # Return number of nodes in "joints" array
    def getNumJoints (self):
        pass

    # Assign X3DRigidJointNode array (using a properly typed node array) to MFNode inputOutput field named "joints"
    def setJoints1 (self, nodes):
        pass

    # Assign single X3DRigidJointNode value (using a properly typed node) as the MFNode array for inputOutput field named "joints"
    def setJoints2 (self, node):
        pass

    # Assign X3DRigidJointNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "joints"
    def setJoints3 (self, node):
        pass

    # Assign X3DRigidJointNode array (using a properly typed node array) to MFNode inputOutput field named "joints"
    def setJoints4 (self, nodes):
        pass

    # Return CollisionCollection result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "collider"
    def getCollider (self, result):
        pass

    # Assign CollisionCollection value (using a properly typed node) to SFNode initializeOnly field named "collider"
    def setCollider (self, node):
        pass

    # Assign CollisionCollection value (using a properly typed protoInstance)
    def setCollider2 (self, protoInstance):
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
