from . import *
from PIL import Image
import numpy
from numpy import array


class CImageTexture(CX3DTexture2DNode):
    m_strNodeName = "ImageTexture"
    url = ""

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.url = ""
        self.m_nTextureCnt = 0

    def setURL(self, value, filepath, m_TextureNode, nTex_Value):
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

        bLoad = False

        length = len(m_TextureNode)
        for i in range(0, length):
            if value == m_TextureNode[i] :
                bLoad = True
                break

        if not bLoad :
            nTex_Value = self.LoadTexture(self.url, self.m_nTextureCnt)

            if nTex_Value >= 0:
                glBindTexture(GL_TEXTURE_2D, nTex_Value)
                self.m_nTextureCnt += 1

            m_TextureNode.append(self.url)

    def LoadTexture(self, file_name, nIdx):
        texName = nIdx

        pBitmap = Image.open(file_name)

        if not pBitmap :
            return 0

        pBitmap = pBitmap.transpose(Image.FLIP_TOP_BOTTOM)

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
        
    def getURL(self):
        return self.url