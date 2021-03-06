# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxDialogue.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class BoxDialogue(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.xLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.xLineEdit.setObjectName("xLineEdit")
        self.verticalLayout_4.addWidget(self.xLineEdit)
        self.yLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.yLineEdit.setObjectName("yLineEdit")
        self.verticalLayout_4.addWidget(self.yLineEdit)
        self.zLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.zLineEdit.setObjectName("zLineEdit")
        self.verticalLayout_4.addWidget(self.zLineEdit)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.OnOkButtonClick)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Box Node Dialogue"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.label_4.setText(_translate("Dialog", "Solid"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.comboBox.setItemText(0, _translate("Dialog", "True"))
        self.comboBox.setItemText(1, _translate("Dialog", "False"))

    def InitData(self, data, solid):
        self.xLineEdit.setText(str(data.x()))
        self.yLineEdit.setText(str(data.y()))
        self.zLineEdit.setText(str(data.z()))
        if solid: self.comboBox.setCurrentIndex(0)
        else: self.comboBox.setCurrentIndex(1)

    def OnOkButtonClick(self):
        self.values = {
            'X': self.xLineEdit.text(),
            'Y': self.yLineEdit.text(),
            'Z': self.zLineEdit.text(),
            'Solid' : self.comboBox.currentText()
        }
        self.accept()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
