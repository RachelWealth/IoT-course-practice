# import matplotlib
#
# matplotlib.use("Qt5Agg")  # 声明使用QT5
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
#
#
# class MyFigure(FigureCanvas):
#     def __init__(self, width=5, height=4, dpi=100):
#         self.fig = Figure(figsize=(width, height), dpi=dpi)
#         super(MyFigure, self).__init__(self.fig)

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('百度')  #窗口标题
        self.setGeometry(5,30,1355,730)  #窗口的大小和位置设置
        self.browser=QWebEngineView()
        #加载外部的web界面
        self.browser.load(QUrl('https://www.baidu.com'))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())
