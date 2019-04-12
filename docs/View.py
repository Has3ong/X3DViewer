
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import QSize, Qt
import sys

class OpenGLView(QOpenGLWidget):
    m_Mode = GL_POLYGON
    p_RGBA = [0.0, 0.0, 0.0, 0.0]
    b_RGBA = [0.0, 0.0, 0.0, 0.0]

    def __init__(self, parent=None):
        super(OpenGLView, self).__init__(parent)

    def initializeGL(self):
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)

        glShadeModel(GL_SMOOTH)
        glEnable(GL_NORMALIZE)

        glClearDepth(1.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

        #glEnable(GL_POINT_SMOOTH)
        #glEnable(GL_LINE_SMOOTH)
        #glEnable(GL_POLYGON_SMOOTH)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
    
    def resizeGL(self, width, height):
    
        # self.aspect = ( height == 0) ? width : (double)width / (double)height
        glGetError()    # uncomment this line when error occurs here

        aspect = width if (height == 0) else width / height

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, aspect, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #glDrawBuffer(GL_BACK)

    def paintGL(self):
        glClearColor(self.b_RGBA[0], self.b_RGBA[1], self.b_RGBA[2], self.b_RGBA[3])
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.update()
        

    def mousePressEvent(self, event):
        self.x_last = event.x()
        self.y_last = event.y()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

    def wheelEvent(self, event):
        self.x = event.x()
        self.y = event.y()
