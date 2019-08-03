from . import *

# SFImage defines an abstract node interface.
# The SFImage field specifies a single uncompressed 2-dimensional pixel image. SFImage fields contain three integers representing the width, height and number of components in the image, followed by (width x height) hexadecimal or integer values representing the pixels in the image.
class CSFImage(CX3DField):
    m_value = 0.0

    def __init__(self):
        m_value = 0.0

    #  Get image width in pixels
    def getWidth (self):
        pass

    #  Get image height in pixels
    def getHeight (self):
        pass

    #  Get number of components in an imag
    #       * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).*/
    def getComponents(self):
        pass

    #  Get array of pixel values [0-255]
    def getPixels (self, pixels):
        pass

    #  Get java.awt.image.WritableRenderedImage version of image
    #     public  java.awt.image.WritableRenderedImage getImage():

    #  Initialize image
    def setValue (self, width,
                  height,
                  components,
                  pixels):
        pass

    # Assign a new image as current image
    def setImage (self, image):
        pass

    # Assign a portion of a new image as part of current image
    def setSubImage (self, image,
                     srcWidth,
                     srcHeight,
                     srcXOffset,
                     srcYOffset,
                     destXOffset,
                     destYOffset):
        pass