from pyqt5_plugins.examplebutton import QtWidgets

from ui.login import Ui_Dialog as loginWin


class signinWidget(QtWidgets.QWidget, loginWin):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.dia = QtWidgets.QDialog()
        self.setupUi()
        # self.setupUi(self)

    def closeEvent(self, event):
        print("X is clicked: hijaSub1")
