from .MyApp import Ui_MainWindow
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import *
import sys


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.m_Mode = GL_POLYGON
        self.flag = 3

        self.setupUi(self)
        self.connectMenu()
        self.connectButton()
        self.connectSlider()

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
        pass

    def OnOpenDocument(self):
        filter = "X3D File (*.x3d);; All Files (*.*)"
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', filter)
        filepath = fname

        '''
        if fname[0]:
            parse = Parser()
            del parse.object[ : ]
            parse.Parsing(fname[0])

        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
        '''

        print("OnOpenDocument")
    def OnCloseDocument(self):
        print("OnCloseDocument")
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
        print("Vertex")
    def OnWire(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(True)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(True)
        self.FaceButton.setChecked(False)

        self.m_Mode = GL_LINE
        self.flag = 2
        print("Wire")
    def OnFace(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(True)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(True)

        self.m_Mode = GL_POLYGON
        self.flag = 3
        print("Face")

