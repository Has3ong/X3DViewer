import sys
from PyQt5.QtWidgets import QApplication

from docs.Window import MyWindow

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

