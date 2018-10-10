#06_QToolTip.py
import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QApplication
from PyQt5.QtGui import QFont,QIcon

class Winform(QWidget):
	"""docstring for Winform"""
	def __init__(self):
		super(Winform, self).__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',16))
		self.setToolTip("This is a <b>Tips</b>")
		self.setGeometry(200,300,400,400)
		self.setWindowTitle("Tips")
		self.setWindowIcon(QIcon("img/book.ico"))
		self.show()

if __name__=="__main__":
	app = QApplication(sys.argv)
	win = Winform()
	sys.exit(app.exec_())