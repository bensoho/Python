#6_01_absoPosition.py
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		lbl1 = QLabel('Welcome to',self)
		lbl1.move(15,10)

		lbl2 = QLabel('Learn',self)
		lbl2.move(35,40)

		lbl3 = QLabel('Python',self)
		lbl3.move(55,70)

		self.setGeometry(300,300,320,120)
		self.setWindowTitle('Absolute position sample')


if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = Example()
	demo.show()
	sys.exit(app.exec_())

