# -*- coding: utf-8 -*-
#主窗口show in center QMainWindow.py

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget

class MainWindow(QMainWindow):
    """docstring for MainWindow"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Main Window Show in Screen Center")
        self.resize(400,200)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        print(size)
        print(screen)
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())



