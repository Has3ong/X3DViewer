from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

class X3DTreeWidget(QTreeWidget):
    def __init__(self, parent):
        return super().__init__(parent)
    
    def DrawTree(self, x3dnode):
        root = QTreeWidgetItem(self)
        root.setText(0, x3dnode.m_strNodeName)
        root.setExpanded(True)
        
        length = len(x3dnode.children)
        for i in range(0, length):
            self.Draw(root, x3dnode.children[i])

    def Draw(self, head, x3dnode):
        print(head, x3dnode)
        item = QTreeWidgetItem(head)
        item.setText(0, x3dnode.m_strNodeName)
        item.setExpanded(True)

        length = len(x3dnode.children)
        for i in range(0, length):
            self.Draw(item, x3dnode.children[i])
        
