# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ViewpointDialogue.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ViewpointDialogue(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 600)
        Dialog.setMinimumSize(QtCore.QSize(400, 600))
        Dialog.setMaximumSize(QtCore.QSize(400, 600))
        Dialog.setMouseTracking(False)
        Dialog.setAcceptDrops(False)
        Dialog.setAccessibleDescription("")
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setAccessibleDescription("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 374, 660))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMinimumSize(QtCore.QSize(80, 200))
        self.groupBox_3.setMaximumSize(QtCore.QSize(80, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setMinimumSize(QtCore.QSize(80, 200))
        self.groupBox_5.setMaximumSize(QtCore.QSize(80, 200))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_13.setMinimumSize(QtCore.QSize(80, 200))
        self.groupBox_13.setMaximumSize(QtCore.QSize(80, 200))
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.groupBox_13)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_15 = QtWidgets.QLabel(self.groupBox_13)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_13)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.verticalLayout_4.addWidget(self.groupBox_13)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.position_xLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.position_xLineEdit.setObjectName("position_xLineEdit")
        self.verticalLayout_9.addWidget(self.position_xLineEdit)
        self.position_yLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.position_yLineEdit.setObjectName("position_yLineEdit")
        self.verticalLayout_9.addWidget(self.position_yLineEdit)
        self.position_zLineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.position_zLineEdit.setObjectName("position_zLineEdit")
        self.verticalLayout_9.addWidget(self.position_zLineEdit)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.orientation_xLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.orientation_xLineEdit.setObjectName("orientation_xLineEdit")
        self.verticalLayout_12.addWidget(self.orientation_xLineEdit)
        self.orientation_yLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.orientation_yLineEdit.setObjectName("orientation_yLineEdit")
        self.verticalLayout_12.addWidget(self.orientation_yLineEdit)
        self.orientation_zLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.orientation_zLineEdit.setObjectName("orientation_zLineEdit")
        self.verticalLayout_12.addWidget(self.orientation_zLineEdit)
        self.orientation_angleLineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.orientation_angleLineEdit.setObjectName("orientation_angleLineEdit")
        self.verticalLayout_12.addWidget(self.orientation_angleLineEdit)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_14.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_14.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_14.setObjectName("groupBox_14")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_14)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.centerofrotation_xLineEdit = QtWidgets.QLineEdit(self.groupBox_14)
        self.centerofrotation_xLineEdit.setObjectName("centerofrotation_xLineEdit")
        self.verticalLayout_5.addWidget(self.centerofrotation_xLineEdit)
        self.centerofrotation_yLineEdit = QtWidgets.QLineEdit(self.groupBox_14)
        self.centerofrotation_yLineEdit.setObjectName("centerofrotation_yLineEdit")
        self.verticalLayout_5.addWidget(self.centerofrotation_yLineEdit)
        self.centerofrotation_zLineEdit = QtWidgets.QLineEdit(self.groupBox_14)
        self.centerofrotation_zLineEdit.setObjectName("centerofrotation_zLineEdit")
        self.verticalLayout_5.addWidget(self.centerofrotation_zLineEdit)
        self.verticalLayout.addWidget(self.groupBox_14)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Viewpoint Node Dialogue"))
        self.groupBox.setTitle(_translate("Dialog", "Fields"))
        self.groupBox_3.setTitle(_translate("Dialog", "position"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.groupBox_5.setTitle(_translate("Dialog", "orientation"))
        self.label_7.setText(_translate("Dialog", "X"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.label_6.setText(_translate("Dialog", "Z"))
        self.label_5.setText(_translate("Dialog", "Angle"))
        self.groupBox_13.setTitle(_translate("Dialog", "centerOfRotation"))
        self.label_17.setText(_translate("Dialog", "X"))
        self.label_15.setText(_translate("Dialog", "Y"))
        self.label_16.setText(_translate("Dialog", "Z"))
        self.groupBox_2.setTitle(_translate("Dialog", "Value"))
        self.groupBox_4.setTitle(_translate("Dialog", "position"))
        self.groupBox_6.setTitle(_translate("Dialog", "orientation"))
        self.groupBox_14.setTitle(_translate("Dialog", "centerOfRotation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
