from PyQt5.QtWidgets import *
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        #Menubar implements
        m_mainMenu = self.menuBar()
        m_fileMenu = m_mainMenu.addMenu('File')
        m_viewMenu = m_mainMenu.addMenu('View')

        #m_fileMenu 'File Open', 'File Close'
        m_openMenu = QAction("File Open", self)
        m_closeMenu = QAction("Close", self)

        m_fileMenu.addAction(m_openMenu)
        m_fileMenu.addAction(m_closeMenu)

        m_openMenu.triggered.connect(self.OnOpenDocument)
        m_closeMenu.triggered.connect(self.OnCloseDocument)

        #m_viewMenu 'Vertex', 'Wire', 'Face'
        m_vertexMenu = QAction("Vertex", self)
        m_wireMenu = QAction("Wire", self)
        m_faceMenu = QAction("Face", self)

        m_viewMenu.addAction(m_vertexMenu)
        m_viewMenu.addAction(m_wireMenu)
        m_viewMenu.addAction(m_faceMenu)

        m_vertexMenu.triggered.connect(self.OnVertex)
        m_wireMenu.triggered.connect(self.OnWire)
        m_faceMenu.triggered.connect(self.OnFace)

        #setGeometry pos(300, 300), size(200, 200)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Example')
        self.show()

    def OnOpenDocument(self):
        print("OnOpenDocument")

    def OnCloseDocument(self):
        print("CloseDocument")
        QApplication.quit()

    def OnVertex(self):
        print("OnVertex")

    def OnWire(self):
        print("OnWire")

    def OnFace(self):
        print("OnFace")
    