import sys
from PyQt5.QtWidgets import *
from application import AppWindow
objs = ['cloth', 'flovoring', 'book']
databases=['cloth', 'flovoring', 'book']






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())





