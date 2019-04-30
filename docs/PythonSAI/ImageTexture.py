import numpy
from . import *
from PIL import Image

class CImageTexture(CX3DTexture2DNode, CX3DUrlObject):
    m_strNodeName = "ImageTexture"
    url = ""
    m_nTextureCnt = 0

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.url = ""
        self.textures = -1

    def Draw(self):
        if self.textures < 0:
            return 0
        else:
            glEnable(GL_TEXTURE_2D)    
            glBindTexture(GL_TEXTURE_2D, self.textures)

    def setURL(self, value, filepath, m_TextureNode):
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

        length = len(m_TextureNode)
        for i in range(0, length):
            if self.url == m_TextureNode[i] :
                self.textures = i
                return 0

        nTex_Value = self.LoadTexture(self.url, CImageTexture.m_nTextureCnt)

        if nTex_Value >= 0:
            #glBindTexture(GL_TEXTURE_2D, nTex_Value)
            self.textures = CImageTexture.m_nTextureCnt
            CImageTexture.m_nTextureCnt += 1

        m_TextureNode.append(self.url)

    def LoadTexture(self, file_name, nIdx):
        texName = nIdx

        pBitmap = Image.open(file_name)
        if not pBitmap :
            return -1

        pBitmap = pBitmap.transpose(Image.FLIP_TOP_BOTTOM)
        pBitmapData = numpy.array(list(pBitmap.getdata()), numpy.int8)

        glGenTextures(1, texName)
        glBindTexture(GL_TEXTURE_2D, texName)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

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

        '''
        pBitmap = pBitmap.convert("RGBA")
        pixel = pBitmap.load()
        for i in range (0, pBitmap.width):
            for j in range (0, pBitmap.height):
                tmp = []
                tmp = list(pixel[i,j])
                pixel[i,j] = (tmp[3], tmp[0], tmp[1], tmp[2])
                tmp.clear()

        pBitmapData = pBitmap.tobytes("raw", "RGBA", 0, -1)
        
        glEnable(GL_TEXTURE_2D)

        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        glGenTextures(nIdx+1, texName)

        glBindTexture(GL_TEXTURE_2D, texName)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, pBitmap.size[0], pBitmap.size[1], 0,
            GL_BGRA, GL_UNSIGNED_BYTE, pBitmapData
            )
        x = glGetError()
        m_nId = texName
        return texName
        '''
        
    def getURL(self):
        return self.url