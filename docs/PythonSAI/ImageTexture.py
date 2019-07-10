import numpy
from . import *
from PIL import Image

# ImageTexture defines a concrete node interface that extends interfaces X3DTexture2DNodeX3DUrlObject.
class CImageTexture(CX3DTexture2DNode, CX3DUrlObject):
    m_strNodeName = "ImageTexture"
    url = ""
    m_nTextureCnt = 0
    m_TextureNode = []

    def __init__(self):
        self.m_strNodeName = "ImageTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
        self.url = ""
        self.textures = -1
        
    def Draw(self):
        if self.textures < 0:
            return 0
        else:
            glEnable(GL_TEXTURE_2D)    
            glBindTexture(GL_TEXTURE_2D, CImageTexture.m_TextureNode[self.textures])

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getURL(self):
        return self.url

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setURL(self, value, filepath):
        strData = filepath
        index = 0
        while 1:
            nDelimiter = 0
            nDelimiter = strData.find('/')
            if nDelimiter < 0:
                filepath = filepath[0:index]
                break
            else:
                strData = strData[nDelimiter + 1 : ]
                index += nDelimiter + 1
        value = filepath + value
        self.url = value

        length = len(CImageTexture.m_TextureNode)
        for i in range(0, length):
            if self.url == CImageTexture.m_TextureNode[i] :
                self.textures = i
                return 0

        nTex_Value = self.LoadTexture(self.url, CImageTexture.m_nTextureCnt, CImageTexture.m_TextureNode)

        if nTex_Value >= 0:
            self.textures = CImageTexture.m_nTextureCnt
            CImageTexture.m_nTextureCnt += 1

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2(self, value):
        pass

    def LoadTexture(self, file_name, nIdx, m_TextureNode):
        texName = nIdx

        pBitmap = Image.open(file_name)
        if not pBitmap :
            return -1

        pBitmap = pBitmap.transpose(Image.FLIP_TOP_BOTTOM)
        pBitmapData = numpy.array(list(pBitmap.getdata()), numpy.int8)

        texName = glGenTextures(1)
        m_TextureNode.append(texName)
        glBindTexture(GL_TEXTURE_2D, texName)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGB, pBitmap.size[0], pBitmap.size[1],
            0, GL_RGB, GL_UNSIGNED_BYTE, pBitmapData
        )

        x = glGetError()

        return texName
        

    def setAttribute(self, Node):
        self.url = Node.url

    def Init(self):
        length = len(CImageTexture.m_TextureNode)
        print(length)
        for i in range(0, length):
            glDeleteTextures(CImageTexture.m_TextureNode[i])

    # ===== methods for fields inherited from parent interfaces =====

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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
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
