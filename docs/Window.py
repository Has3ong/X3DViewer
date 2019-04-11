from .MyApp import Ui_MainWindow

from PyQt5.QtWidgets import *
import sys


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def connectMenu(self):
        pass
    def connectButton(self):
        pass
    def connectSlider(self):
        pass

