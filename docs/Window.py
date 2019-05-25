
from .MyApp import Ui_MainWindow
from .View import OpenGLView
from .PythonSAI import CX3DScene

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OpenGL = OpenGLView(self.groupBox_2)
        #self.OpenGL = QTabWidget()
        #self.OpenGL.setTabsClosable(True)

        self.OpenGL.setObjectName("OpenGL")
        self.gridLayout_5.addWidget(self.OpenGL, 0, 0, 1, 1)
        self.connectMenu()
        self.connectButton()
        self.show()

    def resizeEvent(self, event):
        pass

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

    def OnOpenDocument(self):
        filter = "X3D File (*.x3d);; All Files (*.*)"
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', filter)
        filepath = fname[0]

        if fname[0]:
            idx = filepath.find(".")
            extension = filepath[idx + 1 : ]
            if extension == 'x3d':
                #self.OpenGL.addTab(OpenGLView(), filepath)

                #OpenGLView.Init()
                #OpenGLView.m_pScene.Parsing(filepath)
                #OpenGLView.flag = 1
                #tree = OpenGLView.m_pScene.m_X3DScene

                self.OpenGL.Init()
                self.OpenGL.m_pScene.Parsing(filepath)
                self.OpenGL.flag = 1
                tree = self.OpenGL.m_pScene.m_X3DScene
                self.OnTreeWidget(tree)

            elif extension == 'wrl':
                QMessageBox.about(
                    self, "Warning",
                    "wrl 파서는 개발중에 있습니다."
                    )
            else:
                QMessageBox.about(
                    self, "Warning",
                    "x3d, wrl 외에 다른 확장자 파일을 선택하셨습니다."
                    )
        else:
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")

    def OnTreeWidget(self, x3dtree):
        self.treeWidget.clear()
        self.treeWidget.DrawTree(x3dtree)

    def OnCloseDocument(self):
        QApplication.quit()

    def OnVertex(self):
        self.actionVertex.setChecked(True)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(True)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(False)

        OpenGLView.m_Mode = GL_POINTS

    def OnWire(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(True)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(True)
        self.FaceButton.setChecked(False)

        OpenGLView.m_Mode = GL_LINE

    def OnFace(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(True)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(True)

        OpenGLView.m_Mode = GL_POLYGON