#05_set_icon_for_app.py
import sys,os,imgrcc
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget,QApplication

class IconShow(QWidget):
	"""docstring for Icon"""
	def __init__(self, parent=None):
		super(IconShow, self).__init__(parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(200,200,400,200)
		self.setWindowTitle("ICON")
		self.setWindowIcon(QtGui.QIcon(':/img/book.ico'))

		self.show()


if __name__=="__main__":
	app = QApplication(sys.argv)
	icon = IconShow()
	print(os.getcwd())
	sys.exit(app.exec_())
