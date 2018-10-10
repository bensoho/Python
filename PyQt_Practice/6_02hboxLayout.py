#6_02hboxLayout.py
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Winform(QWidget):
	"""docstring for Winform"""
	def __init__(self, parent = None):
		super(Winform, self).__init__(parent)
		self.setWindowTitle('Vertical layout sample')

		hlayout = QVBoxLayout()

		hlayout.addWidget(QPushButton(str(1)))
		hlayout.addWidget(QPushButton(str(2)))
		hlayout.addWidget(QPushButton(str(3)))
		hlayout.addWidget(QPushButton(str(4)))
		hlayout.addWidget(QPushButton(str(5)))

		hlayout.setSpacing(0)

		self.setLayout(hlayout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = Winform()
	demo.show()
	sys.exit(app.exec_())

