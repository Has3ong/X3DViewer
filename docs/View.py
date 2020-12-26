from .MyApp import Ui_MainWindow
from .PythonSAI.X3DScene import CX3DScene
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT  import *
from PyQt5.QtWidgets import QOpenGLWidget
import time

class OpenGLView(QOpenGLWidget):
    m_pScene = CX3DScene()
    m_Mode = GL_POLYGON
    flag = 0

    width_OpenGL = 0
    height_OpenGL = 0

    m_xRotation = 0.0
    m_yRotation = 0.0
    m_zRotation = 0.0

    m_xTranslation = 0.0
    m_yTranslation = 0.0
    m_zTranslation = -20.0

    m_xScaling = 1.0
    m_yScaling = 1.0
    m_zScaling = 1.0

    m_SpeedRotation = 1.0 / 3.0
    m_SpeedTranslation = 1.0 / 5000.0
    m_SpeedZoom = 1.0 / 1.0

    m_xyRotation = 1

    def __init__(self, parent):
        return super().__init__(parent)
        
    def initializeGL(self):
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)

        glShadeModel(GL_SMOOTH)
        #glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)

        glClearDepth(1.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)

        #glEnable(GL_POINT_SMOOTH)
        #glEnable(GL_LINE_SMOOTH)
        #glEnable(GL_POLYGON_SMOOTH)

        #glEnable(GL_TEXTURE_2D)
    
    def resizeGL(self, width, height):
        #self.aspect = ( height == 0) ? width : (double)width / (double)height
        glGetError()    # uncomment this line when error occurs here

        aspect = width if (height == 0) else width / height

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, aspect, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        if self.m_Mode == GL_POINTS :
            glPolygonMode(GL_FRONT, GL_POINT)
            glPolygonMode(GL_BACK, GL_POINT)
        elif self.m_Mode == GL_LINE :
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        elif self.m_Mode == GL_POLYGON:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        glPushMatrix()
        glTranslatef(self.m_xTranslation, self.m_yTranslation, self.m_zTranslation)
        glRotatef(self.m_xRotation, 1.0, 0.0, 0.0)
        glRotatef(self.m_yRotation, 0.0, 1.0, 0.0)
        glRotatef(self.m_zRotation, 0.0, 0.0, 1.0)
        glScalef(self.m_xScaling, self.m_yScaling, self.m_zScaling)
        self.update()

        if self.flag :
            time.sleep(1 / 20)
            self.m_pScene.Draw()
            
        glPopMatrix()
        glFlush()
        
    def mousePressEvent(self, event):
        self.x_last = event.x()
        self.y_last = event.y()

    def mouseMoveEvent(self, event):
        self.x = event.x()
        self.y = event.y()

        self.m_xRotation -= (float)(self.y - self.y_last) * self.m_SpeedRotation
        self.m_yRotation += (float)(self.x - self.x_last) * self.m_SpeedRotation

        self.x_last = self.x
        self.y_last = self.y
        self.update()


    def wheelEvent(self, event):
        e = []
        e = event.angleDelta()
        width = self.width() / 2
        height = self.height() / 2
        self.x = event.x() - width
        self.y = event.y() - height
        
        if int(e.y()) < 0:
            self.m_zTranslation -= self.m_SpeedZoom
            self.m_zTranslation -= self.m_SpeedZoom

        else:
            self.m_zTranslation += self.m_SpeedZoom
            self.m_zTranslation += self.m_SpeedZoom

        self.m_xTranslation += self.x * self.m_SpeedTranslation
        self.m_yTranslation -= self.y * self.m_SpeedTranslation

        self.update()