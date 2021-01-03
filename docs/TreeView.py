from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

from .Dialogue import *
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

        if nodeName == 'Appearance':
            QMessageBox.about(self, "Warning", "Appearance 속성이 없습니다.")

        elif nodeName == 'Background':
            retData = {}
            dg = BackgroundDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getSkyColor()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setSkyColor(
                    CSFColor([float(retData['rSkyColor']), float(retData['gSkyColor']), float(retData['bSkyColor'])])
                )
            del retData

        elif nodeName == 'Box':
            retData = {}
            dg = BoxDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getSize3(), self.data[id(event)].getSolid()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setSize3([float(retData['X']), float(retData['Y']), float(retData['Z'])])
                self.data[id(event)].setSolid(bool(retData['Solid']))
            del retData

        elif nodeName == 'Cone':
            retData = {}
            dg = ConeDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getHeight(), self.data[id(event)].getBottomRadius(), self.data[id(event)].getSide(),
                self.data[id(event)].getBottom(), self.data[id(event)].getSolid()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setHeight(float(retData['Height']))
                self.data[id(event)].setBottomRadius(float(retData['BottomRadius']))
                self.data[id(event)].setSide(bool(retData['Side']))
                self.data[id(event)].setBottom(bool(retData['Bottom']))
                self.data[id(event)].setSolid(bool(retData['Solid']))
            del retData
        elif nodeName == 'Cylinder':
            retData = {}
            dg = CylinderDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getHeight(), self.data[id(event)].getRadius(), self.data[id(event)].getTop(),
                self.data[id(event)].getSide(), self.data[id(event)].getBottom(), self.data[id(event)].getSolid()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setHeight(float(retData['Height']))
                self.data[id(event)].setRadius(float(retData['Radius']))
                self.data[id(event)].setTop(bool(retData['Top']))
                self.data[id(event)].setSide(bool(retData['Side']))
                self.data[id(event)].setBottom(bool(retData['Bottom']))
                self.data[id(event)].setSolid(bool(retData['Solid']))
            del retData

        elif nodeName == 'head':
            QMessageBox.about(self, "Warning", "head 속성이 없습니다.")

        elif nodeName == 'Material':
            retData = {}
            dg = MaterialDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getAmbientIntensity(), self.data[id(event)].getShininess(), self.data[id(event)].getTransparency(),
                self.data[id(event)].getDiffuseColor(), self.data[id(event)].getEmissiveColor(), self.data[id(event)].getSpecularColor()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setAmbientIntensity(float(retData['AmbientIntensity']))
                self.data[id(event)].setShininess(float(retData['Shininess']))
                self.data[id(event)].setTransparency(float(retData['Transparency']))
                self.data[id(event)].setDiffuseColor(
                    CSFColor([float(retData['rDiffuseColor']), float(retData['gDiffuseColor']), float(retData['bDiffuseColor'])])
                )
                self.data[id(event)].setEmissiveColor(
                    CSFColor([float(retData['rEmissiveColor']), float(retData['gEmissiveColor']), float(retData['bEmissiveColor'])])
                )
                self.data[id(event)].setSpecularColor(
                    CSFColor([float(retData['rSpecularColor']), float(retData['gSpecularColor']), float(retData['bSpecularColor'])])
                )
            del retData

        elif nodeName == 'meta':
            QMessageBox.about(self, "Warning", "meta 속성이 없습니다.")

        elif nodeName == 'Sphere':
            retData = {}
            dg = SphereDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getRadius(), self.data[id(event)].getSolid()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setRadius(float(retData['Radius']))
                self.data[id(event)].setSolid(bool(retData['Solid']))
            del retData

        elif nodeName == 'Transform':
            retData = {}
            dg = TransformDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getRotation(), self.data[id(event)].getScale(), self.data[id(event)].getTranslation()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setOrientation(
                    CSFRotation(float(retData['xOrientation']), float(retData['yOrientation']),
                                float(retData['zOrientation']), float(retData['angleOrientation']))
                )
                self.data[id(event)].setPosition(
                    CSFVec3f(float(retData['xPosition']), float(retData['yPosition']), float(retData['zPosition']))
                )
                self.data[id(event)].setScale(
                    CSFVec3f(float(retData['xScale']), float(retData['yScale']), float(retData['zScale']))
                )
            del retData

        elif nodeName == 'Viewpoint':
            retData = {}
            dg = ViewpointDialogue()
            dg.show()
            dg.InitData(
                self.data[id(event)].getOrientation(), self.data[id(event)].getPosition(), self.data[id(event)].getCenterOfRotation()
            )
            if dg.exec_():
                retData = dg.values
                self.data[id(event)].setOrientation(
                    CSFRotation(float(retData['xOrientation']), float(retData['yOrientation']), float(retData['zOrientation']), float(retData['angleOrientation']))
                )
                self.data[id(event)].setPosition(
                    CSFVec3f(float(retData['xPosition']), float(retData['yPosition']), float(retData['zPosition']))
                )
                self.data[id(event)].setCenterOfRotation(
                    CSFVec3f(float(retData['xCenterOfRotation']), float(retData['yCenterOfRotation']), float(retData['zCenterOfRotation']))
                )
            del retData


        else:
            QMessageBox.about(self, "Warning", "미구현")

