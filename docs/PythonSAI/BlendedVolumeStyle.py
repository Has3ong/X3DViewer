from . import *

# BlendedVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CBlendedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "BlendedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "BlendedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from  type inputOutput field named "weightConstant1"
    def getWeightConstant1 (self):
        pass

    # Assign float value [] to  type inputOutput field named "weightConstant1"
    def setWeightConstant1 (self, value):
        pass

    # Return float result [] from  type inputOutput field named "weightConstant2"
    def getWeightConstant2 (self):
        pass

    # Assign float value [] to  type inputOutput field named "weightConstant2"
    def setWeightConstant2 (self, value):
        pass

    # Return String enumeration result ("CONSTANT"|"ALPHA1"|"ALPHA2"|"ONE_MINUS_ALPHA1"|"ONE_MINUS_ALPHA2"|"TABLE") from volumeRenderingWeightFunctionTypes type inputOutput field named "weightFunction1"
    def getWeightFunction1 (self):
        pass

    # Assign String enumeration value ("CONSTANT"|"ALPHA1"|"ALPHA2"|"ONE_MINUS_ALPHA1"|"ONE_MINUS_ALPHA2"|"TABLE") to volumeRenderingWeightFunctionTypes type inputOutput field named "weightFunction1"
    def setWeightFunction1 (self, value):
        pass

    # Return String enumeration result ("CONSTANT"|"ALPHA1"|"ALPHA2"|"ONE_MINUS_ALPHA1"|"ONE_MINUS_ALPHA2"|"TABLE") from volumeRenderingWeightFunctionTypes type inputOutput field named "weightFunction2"
    def getWeightFunction2 (self):
        pass

    # Assign String enumeration value ("CONSTANT"|"ALPHA1"|"ALPHA2"|"ONE_MINUS_ALPHA1"|"ONE_MINUS_ALPHA2"|"TABLE") to volumeRenderingWeightFunctionTypes type inputOutput field named "weightFunction2"
    def setWeightFunction2 (self, value):
        pass

    # Return X3DComposableVolumeRenderStyleNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "renderStyle"
    def getRenderStyle (self, result):
        pass

    # Assign X3DComposableVolumeRenderStyleNode value (using a properly typed node) to SFNode inputOutput field named "renderStyle"
    def setRenderStyle1 (self, node):
        pass

    # Assign X3DComposableVolumeRenderStyleNode value (using a properly typed protoInstance)
    def setRenderStyle2 (self, protoInstance):
        pass

    # Return X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "voxels"
    def getVoxels (self, result):
        pass

    # Assign X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "voxels"
    def setVoxels1 (self, node):
        pass

    # Assign X3DTexture3DNode value (using a properly typed protoInstance)
    def setVoxels2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "weightTransferFunction1"
    def getWeightTransferFunction1 (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "weightTransferFunction1"
    def setWeightTransferFunction1 (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setWeightTransferFunction2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "weightTransferFunction2"
    def getWeightTransferFunction2 (self, result):
        pass

    # Assign X3DTexture2DNode value (using a properly typed node) to SFNode inputOutput field named "weightTransferFunction2"
    def setWeightTransferFunction3 (self, node):
        pass

    # Assign X3DTexture2DNode value (using a properly typed protoInstance)
    def setWeightTransferFunction4 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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
