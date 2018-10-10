#7.3.2_winSignalSlot04.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget,QMessageBox, QApplication, QHBoxLayout
import sys


class WinForm(QMainWindow):
	"""docstring for WinForm"""
	def __init__(self):
		super(WinForm, self).__init__()

		button1 = QPushButton('button1',self)
		button2 = QPushButton('button2',self)
		button3 = QPushButton('button3',self)
		button1.clicked.connect(lambda:self.onBtnClick(1))
		button2.clicked.connect(lambda:self.onBtnClick(2))
		button3.clicked.connect(self.close)

		layout = QHBoxLayout()
		layout.addWidget(button1)
		layout.addWidget(button2)
		layout.addWidget(button3)
		main_frame = QWidget()
		main_frame.setLayout(layout)
		self.setCentralWidget(main_frame)
	def onBtnClick(self,n):
		print('Button {0} has been pressed.'.format(n))
		QMessageBox.information(self,'INFO alert','Button {0} clicked'.format(n))


if __name__ == "__main__":

	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
