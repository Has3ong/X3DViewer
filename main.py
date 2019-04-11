import sys
from PyQt5.QtWidgets import QApplication

from docs.Window import UI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())

