# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGroupBox(self.centralwidget)
        self.Base.setTitle("")
        self.Base.setObjectName("Base")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Base)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.Base)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.OpenButton = QtWidgets.QPushButton(self.groupBox)
        self.OpenButton.setObjectName("OpenButton")
        self.horizontalLayout_2.addWidget(self.OpenButton)
        self.VertexButton = QtWidgets.QPushButton(self.groupBox)
        self.VertexButton.setCheckable(True)
        self.VertexButton.setAutoRepeat(False)
        self.VertexButton.setAutoExclusive(False)
        self.VertexButton.setObjectName("VertexButton")
        self.horizontalLayout_2.addWidget(self.VertexButton)
        self.WireButton = QtWidgets.QPushButton(self.groupBox)
        self.WireButton.setCheckable(True)
        self.WireButton.setAutoRepeat(False)
        self.WireButton.setAutoExclusive(False)
        self.WireButton.setObjectName("WireButton")
        self.horizontalLayout_2.addWidget(self.WireButton)
        self.FaceButton = QtWidgets.QPushButton(self.groupBox)
        self.FaceButton.setCheckable(True)
        self.FaceButton.setChecked(False)
        self.FaceButton.setAutoRepeat(False)
        self.FaceButton.setAutoExclusive(False)
        self.FaceButton.setObjectName("FaceButton")
        self.horizontalLayout_2.addWidget(self.FaceButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Base)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.OpenGL = QtWidgets.QWidget(self.groupBox_2)
        self.OpenGL.setObjectName("OpenGL")
        self.gridLayout_5.addWidget(self.OpenGL, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Base)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Slider_Primitive_R = QtWidgets.QSlider(self.groupBox_3)
        self.Slider_Primitive_R.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Primitive_R.setObjectName("Slider_Primitive_R")
        self.verticalLayout_4.addWidget(self.Slider_Primitive_R)
        self.Slider_Primitive_G = QtWidgets.QSlider(self.groupBox_3)
        self.Slider_Primitive_G.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Primitive_G.setObjectName("Slider_Primitive_G")
        self.verticalLayout_4.addWidget(self.Slider_Primitive_G)
        self.Slider_Primitive_B = QtWidgets.QSlider(self.groupBox_3)
        self.Slider_Primitive_B.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Primitive_B.setObjectName("Slider_Primitive_B")
        self.verticalLayout_4.addWidget(self.Slider_Primitive_B)
        self.Slider_Primitive_A = QtWidgets.QSlider(self.groupBox_3)
        self.Slider_Primitive_A.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Primitive_A.setObjectName("Slider_Primitive_A")
        self.verticalLayout_4.addWidget(self.Slider_Primitive_A)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Base)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Slider_Background_R = QtWidgets.QSlider(self.groupBox_4)
        self.Slider_Background_R.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Background_R.setObjectName("Slider_Background_R")
        self.verticalLayout_3.addWidget(self.Slider_Background_R)
        self.Slider_Background_G = QtWidgets.QSlider(self.groupBox_4)
        self.Slider_Background_G.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Background_G.setObjectName("Slider_Background_G")
        self.verticalLayout_3.addWidget(self.Slider_Background_G)
        self.Slider_Background_B = QtWidgets.QSlider(self.groupBox_4)
        self.Slider_Background_B.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Background_B.setObjectName("Slider_Background_B")
        self.verticalLayout_3.addWidget(self.Slider_Background_B)
        self.Slider_Background_A = QtWidgets.QSlider(self.groupBox_4)
        self.Slider_Background_A.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Background_A.setObjectName("Slider_Background_A")
        self.verticalLayout_3.addWidget(self.Slider_Background_A)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 6)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Base, 0, 1, 1, 1)
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_3.raise_()
        self.Base.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVertex = QtWidgets.QAction(MainWindow)
        self.actionVertex.setCheckable(True)
        self.actionVertex.setObjectName("actionVertex")
        self.actionWire = QtWidgets.QAction(MainWindow)
        self.actionWire.setCheckable(True)
        self.actionWire.setObjectName("actionWire")
        self.actionFace = QtWidgets.QAction(MainWindow)
        self.actionFace.setCheckable(True)
        self.actionFace.setObjectName("actionFace")
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionFileOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionVertex)
        self.menuView.addAction(self.actionWire)
        self.menuView.addAction(self.actionFace)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VR LAB"))
        self.OpenButton.setText(_translate("MainWindow", "FileOpen"))
        self.VertexButton.setText(_translate("MainWindow", "Vertex"))
        self.WireButton.setText(_translate("MainWindow", "Wire"))
        self.FaceButton.setText(_translate("MainWindow", "Face"))
        self.groupBox_2.setTitle(_translate("MainWindow", "View"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Primitive"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Background"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionVertex.setText(_translate("MainWindow", "Vertex"))
        self.actionWire.setText(_translate("MainWindow", "Wire"))
        self.actionFace.setText(_translate("MainWindow", "Face"))
        self.actionFileOpen.setText(_translate("MainWindow", "FileOpen"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''

