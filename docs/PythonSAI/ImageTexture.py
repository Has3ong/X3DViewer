import numpy
from . import *
from PIL import Image

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
 
        self.url = ""
        self.textures = -1
        
    def Draw(self):
        if self.textures < 0:
            return 0
        else:
            glEnable(GL_TEXTURE_2D)    
            glBindTexture(GL_TEXTURE_2D, CImageTexture.m_TextureNode[self.textures])

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
        
    def getURL(self):
        return self.url

    def setAttribute(self, Node):
        self.url = Node.url

    def Init(self):
        length = len(CImageTexture.m_TextureNode)
        print(length)
        for i in range(0, length):
            glDeleteTextures(CImageTexture.m_TextureNode[i])