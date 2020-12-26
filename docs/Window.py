
from .MyApp import Ui_MainWindow
from .View import OpenGLView
from .PythonSAI import CX3DScene
from .toX3D import WriteX3DFile

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from collections import deque


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OpenGL = OpenGLView(self.groupBox_2)
        self.OpenGL.setObjectName("OpenGL")
        self.gridLayout_7.addWidget(self.OpenGL, 0, 0, 1, 1)
        self.connectMenu()
        self.connectWidget()
        self.show()

    def resizeEvent(self, event):
        pass

    def connectMenu(self):
        self.actionFileOpen.triggered.connect(self.OnOpenDocument)
        self.actionClose.triggered.connect(self.OnCloseDocument)
        self.actionVertex.triggered.connect(self.OnVertex)
        self.actionWire.triggered.connect(self.OnWire)
        self.actionFace.triggered.connect(self.OnFace)
        self.actionToX3D.triggered.connect(self.OnExportX3D)
        self.actionToWRL.triggered.connect(self.OnExportWRL)

    def connectWidget(self):
        self.OpenButton.clicked.connect(self.OnOpenDocument)
        self.VertexButton.clicked.connect(self.OnVertex)
        self.WireButton.clicked.connect(self.OnWire)
        self.FaceButton.clicked.connect(self.OnFace)
        self.tabWidget.tabBarClicked.connect(self.OnTabWidget)

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

                self.OpenGL.m_pScene.Parsing(filepath)
                self.OpenGL.flag = 1
                self.OnTreeWidget(self.OpenGL.m_pScene.m_X3DScene)

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
        self.X3DTreeWidget.clear()
        self.X3DTreeWidget.DrawTree(x3dtree)
        print(self.X3DTreeWidget.data)

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

    def OnExportX3D(self):
        if self.OpenGL.m_pScene.m_X3DScene.children:
            saveFilePath = QFileDialog.getSaveFileName(self, 'Save File', filter="X3D Files (*.x3d)")
            try:
                with open(saveFilePath[0], 'w') as f:
                    f.write("""<?xml version="1.0" encoding="UTF-8"?>\n""")
                    f.write("""<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 3.3//EN" "https://www.web3d.org/specifications/x3d-3.3.dtd">\n""")
                    WriteX3DFile(f, self.OpenGL.m_pScene.m_X3DScene)
            except Exception as e:
                QMessageBox.about(self, "Warning", "X3D 파일을 저장하는데 실패했습니다.")
                return
            else:
                QMessageBox.about(self, "Warning", "저장이 완료되었습니다.")
        else:
            QMessageBox.about(self, "Warning", "Open the X3D File")

    def OnExportWRL(self):
        QMessageBox.about(
            self, "Warning",
            "Not Implement"
        )

    def OnTabWidget(self):
        if self.tabWidget.currentIndex() == 1: OpenGLView.flag = 0
        else: OpenGLView.flag = 1