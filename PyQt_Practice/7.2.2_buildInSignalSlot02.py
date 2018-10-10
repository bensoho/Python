#7.2.2_buildInSignalSlot02.py
from PyQt5.QtWidgets import *
import sys


class WinForm(QWidget):
	"""docstring for WinForm"""
	def __init__(self):
		super(WinForm, self).__init__()
		self.setWindowTitle('BuildIn Signal & Customed Slot Sample')
		self.resize(300,100)
		btn = QPushButton('close',self)
		btn.clicked.connect(self.btn_close)

	def btn_close(self):
		self.close()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
