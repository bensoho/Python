#7.2.3_customized_signal & builtIn_slot.py
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import sys


class WinForm(QWidget):
	"""docstring for WinForm"""
	#创建一个信号对象
	btn_clicked_signal = pyqtSignal(str)

	def __init__(self):
		super(WinForm, self).__init__()
		self.setWindowTitle('Customized Signal and builtIn_Slot')
		self.resize(300,100)
		#创建一个按钮对象
		btn = QPushButton('close',self)
		#点击按钮触发一个（btn_slicked）的信号
		btn.clicked.connect(self.btn_clicked)
		#信号与槽函数建立连接
		self.btn_clicked_signal.connect(self.btn_close)

		#发送自定义信号
	def btn_clicked(self):
		self.btn_clicked_signal.emit('send a Signal')

		#接受自定义信号
	def btn_close(self,msg):
		print(msg)



	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec())



