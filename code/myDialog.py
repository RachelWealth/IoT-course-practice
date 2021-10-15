from PyQt5.QtWidgets import *
from pyqt5_plugins.examplebutton import QtWidgets
from PyQt5 import QtCore


class myDialog(QtWidgets.QDialog):
    my_Signal = QtCore.pyqtSignal(str)

    def __sendCloseSignal__(self):
        closed = '1'
        self.my_Signal.emit(closed)

    def closeEvent(self, event):
        self.__sendCloseSignal__()
