from . import *

# MovieTexture defines a concrete node interface that extends interfaces X3DSoundSourceNodeX3DTexture2DNode, X3DUrlObject.
class CMovieTexture(CX3DTexture2DNode, CX3DUrlObject):
    m_strNodeName = "MovieTexture"
    def __init__(self):
        self.m_strNodeName = "MovieTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getUrl (self):
        pass

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2 (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "repeatS"
    def getRepeatS (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "repeatS"
    def setRepeatS (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "repeatT"
    def getRepeatT (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "repeatT"
    def setRepeatT (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "speed"
    def getSpeed (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "speed"
    def setSpeed (self, value):
        pass

    # Return TextureProperties result (using a properly typed node or X3DPrototypeInstance) from SFNode initializeOnly field named "textureProperties"
    def getTextureProperties (self, result):
        pass

    # Assign TextureProperties value (using a properly typed node) to SFNode initializeOnly field named "textureProperties"
    def setTextureProperties1 (self, node):
        pass

    # Assign TextureProperties value (using a properly typed protoInstance)
    def setTextureProperties2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return double result in seconds from SFTime outputOnly field named "duration_changed"
    def getDuration (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        pass

    # Return float result [] from  type inputOutput field named "pitch"
    def getPitch (self):
        pass

    # Assign float value [] to  type inputOutput field named "pitch"
    def setPitch (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "elapsedTime"
    def getElapsedTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isPaused"
    def getIsPaused (self):
        pass

    # Return boolean result from SFBool inputOutput field named "loop"
    def getLoop (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "loop"
    def setLoop (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "pauseTime"
    def getPauseTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "pauseTime"
    def setPauseTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "resumeTime"
    def getResumeTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "resumeTime"
    def setResumeTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "startTime"
    def getStartTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "startTime"
    def setStartTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "stopTime"
    def getStopTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "stopTime"
    def setStopTime (self, timestamp):
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
