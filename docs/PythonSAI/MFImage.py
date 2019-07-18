from . import *

# MFImage defines an abstract node interface.
# MFImage is an array of SFImage values.
class CMFImage (CMField) :

    # Get selected image width in pixels
    def getWidth (self, imageIndex):
        pass

    # Get selected image height in pixels
    def getHeight (self, imageIndex):
        pass

    # Get number of components in selected image:
        # * 1 (intensity), 2 (intensity alpha), 3 (red green blue), 4 (red green blue alpha-opacity).
    def getComponents (self, imageIndex):
        pass

    # Get array of pixel values [0-255] in selected image
    def getPixels (self, imageIndex, pixels):
        pass

    # Get <a href="http://docs.oracle.com/javase/8/docs/api/java/awt/image/WritableRenderedImage.html">java.awt.image.WritableRenderedImage</a> version of selected image
    def getImage(self, imageIndex):
        pass

    # Assign a new image as a replacement image within the current image array
    def setImage1 (self, imageIndex, img):
        pass

    # Assign a portion of a new image as part of current selected image in array
    def setSubImage (self, imageIndex,
                     img,
                     srcWidth,
                     srcHeight,
                     srcXOffset,
                     srcYOffset,
                     destXOffset,
                     destYOffset):
        pass

    # Utility method to set all values for selected image in array
    def setValue1 (self, imageIndex, value):
        pass

    # Initialize selected image
    def setValue2 (self, imageIndex,
                   width,
                   height,
                   components,
                   pixels):
        pass

    # Utility method to set all values for all images in array
    def setValue3 (self, value):
        pass

    # Assign a new image array as current image array
    def setImage2 (self, img):
        pass

    # Append a new image to current image array
    def append (self, value):
        pass

    # Insert a new image in the current image array
    def insertValue (self, imageIndex, value):
        pass