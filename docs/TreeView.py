from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt
from .Dialogue.BoxDialogue import BoxDialogue
import sys

class X3DTreeWidget(QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setItemsExpandable(False)
        self.data = {}
        self.connectItem()

    def DrawTree(self, x3dnode):
        root = QTreeWidgetItem(self)
        root.setText(0, x3dnode.m_strNodeName)
        root.setExpanded(True)
        
        length = len(x3dnode.children)
        for i in range(0, length):
            self.Draw(root, x3dnode.children[i])

    def Draw(self, head, x3dnode):
        item = QTreeWidgetItem(head)
        item.setText(0, x3dnode.m_strNodeName)
        item.setExpanded(True)
        self.data[id(item)] = x3dnode

        length = len(x3dnode.children)
        for i in range(0, length):
            self.Draw(item, x3dnode.children[i])

    def connectItem(self):
        self.itemDoubleClicked.connect(self.OnDoubleClickItem)

    def OnDoubleClickItem(self, event):
        nodeName = self.data[id(event)].getNodeName()
        if nodeName == 'Box':
            retData = {}
            dg = BoxDialogue()
            dg.show()
            dg.InitData(self.data[id(event)].getSize3())
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setSize3([float(retData['X']), float(retData['Y']), float(retData['Z'])])
        else:
            QMessageBox.about(self, "Warning", "미구현")

