from . import *

# ParticleSystem defines a concrete node interface that extends interface X3DShapeNode.
class CParticleSystem(CX3DShapeNode):
    m_strNodeName = "ParticleSystem"
    def __init__(self):
        self.m_strNodeName = "ParticleSystem"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "createParticles"
    def getCreateParticles (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "createParticles"
    def setCreateParticles (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "lifetimeVariation"
    def getLifetimeVariation (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "lifetimeVariation"
    def setLifetimeVariation (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "maxParticles"
    def getMaxParticles (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "maxParticles"
    def setMaxParticles (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "particleLifetime"
    def getParticleLifetime (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "particleLifetime"
    def setParticleLifetime (self, value):
        pass

    # Return array of 2-tuple float results array [] from SFVec2f inputOutput field named "particleSize"
    def getParticleSize (self, result):
        pass

    # Assign 2-tuple float array [] to SFVec2f inputOutput field named "particleSize"
    def setParticleSize (self, value):
        pass

    # Return array of float results array using RGB values [0..1] from MFFloat initializeOnly field named "colorKey"
    def getColorKey (self):
        pass

    # Return number of primitive values in "colorKey" array
    def getNumColorKey (self):
        pass

    # Assign float array using RGB values [0..1] to MFFloat initializeOnly field named "colorKey"
    def setColorKey1 (self, colors, size):
        pass

    # Assign single float value using RGB values [0..1] as the MFFloat array for initializeOnly field named "colorKey"
    def setColorKey2 (self, color):
        pass

    # Return String result [] from SFString initializeOnly field named "geometryType"
    def getGeometryType (self):
        pass

    # Assign String value [] to SFString initializeOnly field named "geometryType"
    def setGeometryType (self, value):
        pass

    # Return array of float results array [] from MFFloat initializeOnly field named "texCoordKey"
    def getTexCoordKey (self):
        pass

    # Return number of primitive values in "texCoordKey" array
    def getNumTexCoordKey (self):
        pass

    # Assign float array [] to MFFloat initializeOnly field named "texCoordKey"
    def setTexCoordKey1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for initializeOnly field named "texCoordKey"
    def setTexCoordKey2 (self, value):
        pass

    # Return array of X3DParticlePhysicsModelNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode initializeOnly field named "physics"
    def getPhysics (self, result):
        pass

    # Return number of nodes in "physics" array
    def getNumPhysics (self):
        pass

    # Assign X3DParticlePhysicsModelNode array (using a properly typed node array) to MFNode initializeOnly field named "physics"
    def setPhysics1 (self, nodes):
        pass

    # Assign single X3DParticlePhysicsModelNode value (using a properly typed node) as the MFNode array for initializeOnly field named "physics"
    def setPhysics2 (self, node):
        pass

    # Assign X3DParticlePhysicsModelNode array (using a properly typed protoInstance array) to MFNode initializeOnly field named "physics"
    def setPhysics3 (self, node):
        pass

    # Assign X3DParticlePhysicsModelNode array (using a properly typed node array) to MFNode initializeOnly field named "physics"
    def setPhysics4 (self, nodes):
        pass

    # Return X3DAppearanceNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "appearance"
    def getAppearance (self, result):
        pass

    # Assign X3DAppearanceNode value (using a properly typed node) to SFNode inputOutput field named "appearance"
    def setAppearance1 (self, node):
        pass

    # Assign X3DAppearanceNode value (using a properly typed protoInstance)
    def setAppearance2 (self, protoInstance):
        pass

    # Return X3DGeometryNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "geometry"
    def getGeometry (self, result):
        pass

    # Assign X3DGeometryNode value (using a properly typed node) to SFNode inputOutput field named "geometry"
    def setGeometry1 (self, node):
        pass

    # Assign X3DGeometryNode value (using a properly typed protoInstance)
    def setGeometry2 (self, protoInstance):
        pass

    # Return X3DColorNode result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "colorRamp"
    def getColorRamp (self, result):
        pass

    # Assign X3DColorNode value (using a properly typed node) to SFNode initializeOnly field named "colorRamp"
    def setColorRamp1 (self, color):
        pass

    # Assign X3DColorNode value (using a properly typed protoInstance)
    def setColorRamp2 (self, protoInstance):
        pass

    # Return X3DParticleEmitterNode result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "emitter"
    def getEmitter (self, result):
        pass

    # Assign X3DParticleEmitterNode value (using a properly typed node) to SFNode initializeOnly field named "emitter"
    def setEmitter1 (self, node):
        pass

    # Assign X3DParticleEmitterNode value (using a properly typed protoInstance)
    def setEmitter2 (self, protoInstance):
        pass

    # Return TextureCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "texCoordRamp"
    def getTexCoordRamp (self, result):
        pass

    # Assign TextureCoordinate value (using a properly typed node) to SFNode initializeOnly field named "texCoordRamp"
    def setTexCoordRamp1 (self, node):
        pass

    # Assign TextureCoordinate value (using a properly typed protoInstance)
    def setTexCoordRamp2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "bboxCenter"
    def getBboxCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "bboxCenter"
    def setBboxCenter (self, value):
        pass

    # Return array of 3-tuple float results array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 from boundingBoxSizeType type initializeOnly field named "bboxSize"
    def getBboxSize (self):
        pass

    # Assign 3-tuple float array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 to boundingBoxSizeType type initializeOnly field named "bboxSize"
    def setBboxSize (self, value):
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
