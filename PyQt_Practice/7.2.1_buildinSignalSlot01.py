#7.2.1_buildinSignalSlot01.py
from PyQt5.QtWidgets import *
import sys


class WinForm(QWidget):
	"""docstring for WinForm"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle('BuildIn sigal/slot sample')
		self.resize(330,50)
		btn = QPushButton('close',self)
		btn.clicked.connect(self.close)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec())

