from pyqt5_plugins.examplebutton import QtWidgets

from ui.login import Ui_Dialog as loginWin
from PyQt5.QtWidgets import *
import sys
from myDialog import myDialog


class signinWidget(QWidget, loginWin):
    def __init__(self, parent=None):
        super(signinWidget, self).__init__(parent)
        self.dia = myDialog()
        self.setupUi(self.dia)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = signinWidget()
    win.dia.show()
    sys.exit(app.exec_())