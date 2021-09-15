# coding:utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(960,700)
        self.main_widget = QtWidgets.QWidget() # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout() # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout) # 设置窗口主部件布局为网格布局
        self.left_widget = QtWidgets.QWidget() # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout() # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件

        self.left_management = QtWidgets.QPushButton("管理")
        self.left_management.setObjectName('left_button_1')
        self.left_add = QtWidgets.QPushButton("添加")
        self.left_add.setObjectName('left_button_1')

        self.left_label_1 = QtWidgets.QPushButton("衣服")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("调料")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("图书")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton("颜色")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton("材质")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton("季节")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton("调料1")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton("调料2")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton("调料3")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton("图书1")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton("图书2")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton("图书3")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_management, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_add, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:20px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid white;font-weight:700;}
            QPushButton#left_button_1:hover{font-weight:700;}
            QWidget#left_widget{
                background:#00bfff;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#87CEFA;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
        ''')
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()