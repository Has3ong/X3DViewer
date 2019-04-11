from PyQt5.QtWidgets import *
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        #setGeometry pos(300, 300), size(200, 200)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Example')
        self.show()





