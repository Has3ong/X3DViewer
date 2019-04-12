from .MyApp import Ui_MainWindow
from .View import OpenGLView

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

class MyWindow(QMainWindow, Ui_MainWindow, OpenGLView):
    def __init__(self):
        super().__init__()
    
        self.setupUi(self)
        self.connectMenu()
        self.connectButton()
        self.connectSlider()

        self.glwidget = OpenGLView(parent=self.OpenGL)
        self.show()
        self.glwidget.setFixedSize(850, 600)
        self.show()

        self.init()

    def init(self):
        self.Slider_Background_R.setValue(self.b_RGBA[0] * 256)
        self.Slider_Background_G.setValue(self.b_RGBA[1] * 256)
        self.Slider_Background_B.setValue(self.b_RGBA[2] * 256)
        self.Slider_Background_A.setValue(self.b_RGBA[3] * 256)
        self.Slider_Primitive_R.setValue(self.p_RGBA[0] * 256)
        self.Slider_Primitive_G.setValue(self.p_RGBA[1] * 256)
        self.Slider_Primitive_B.setValue(self.p_RGBA[2] * 256)
        self.Slider_Primitive_A.setValue(self.p_RGBA[3] * 256)

    def resizeEvent(self, event):
        self.qwidth = self.groupBox_2.width() - 10
        self.qheight = self.groupBox_2.height() - 10
        self.glwidget.setFixedSize(self.qwidth, self.qheight)
        self.show()

    def connectMenu(self):
        self.actionFileOpen.triggered.connect(self.OnOpenDocument)
        self.actionClose.triggered.connect(self.OnCloseDocument)
        self.actionVertex.triggered.connect(self.OnVertex)
        self.actionWire.triggered.connect(self.OnWire)
        self.actionFace.triggered.connect(self.OnFace)

    def connectButton(self):
        self.OpenButton.clicked.connect(self.OnOpenDocument)
        self.VertexButton.clicked.connect(self.OnVertex)
        self.WireButton.clicked.connect(self.OnWire)
        self.FaceButton.clicked.connect(self.OnFace)

    def connectSlider(self):
        self.Slider_Primitive_R.valueChanged.connect(self.OnPR)
        self.Slider_Primitive_G.valueChanged.connect(self.OnPG)
        self.Slider_Primitive_B.valueChanged.connect(self.OnPB)
        self.Slider_Primitive_A.valueChanged.connect(self.OnPA)
        
        self.Slider_Background_R.valueChanged.connect(self.OnBR)
        self.Slider_Background_G.valueChanged.connect(self.OnBG)
        self.Slider_Background_B.valueChanged.connect(self.OnBB)
        self.Slider_Background_A.valueChanged.connect(self.OnBA)

    def OnOpenDocument(self):
        filter = "X3D File (*.x3d);; All Files (*.*)"
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', filter)
        filepath = fname

        if fname[0]:
            QMessageBox.about(self, "Warning", fname[0])
        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
        
    def OnCloseDocument(self):
        QApplication.quit()

    def OnVertex(self):
        self.actionVertex.setChecked(True)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(True)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(False)

        self.m_Mode = GL_POINTS
        self.flag = 1

    def OnWire(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(True)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(True)
        self.FaceButton.setChecked(False)

        self.m_Mode = GL_LINE
        self.flag = 2

    def OnFace(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(True)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(True)

        self.m_Mode = GL_POLYGON
        self.flag = 3

    def OnPR(self):
        self.p_RGBA[0] = self.Slider_Primitive_R.value() / 256
    
    def OnPG(self):
        self.p_RGBA[1] = self.Slider_Primitive_G.value() / 256

    def OnPB(self):
        self.p_RGBA[2] = self.Slider_Primitive_B.value() / 256

    def OnPA(self):
        self.p_RGBA[3] = self.Slider_Primitive_A.value() / 256

    def OnBR(self):
        self.b_RGBA[0] = self.Slider_Background_R.value() / 256

    def OnBG(self):
        self.b_RGBA[1] = self.Slider_Background_G.value() / 256

    def OnBB(self):
        self.b_RGBA[2] = self.Slider_Background_B.value() / 256

    def OnBA(self):
        self.b_RGBA[3] = self.Slider_Background_A.value() / 256
        


