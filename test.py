import sys,os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon,QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # x轴位置，y轴位置,x轴长度，y轴长度
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon("1"))
        self.setWindowIcon(QIcon(QPixmap('')))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__),'1.ico')
    print(path)

    ex = Example()
    
    sys.exit(app.exec_())