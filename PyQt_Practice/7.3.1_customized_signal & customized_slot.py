#7.3.1_customized_signal & customized_slot.py

#声明信号对象，定义槽函数，连接信号与槽函数，发射信号

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QPushButton,QWidget,QApplication
import sys

class CustSignal(QWidget):
	"""docstring for CustSignal"""
	signal = pyqtSignal(int)

	def getValue(self,value):
		print('Emit Signal Value:',value)

	def __init__(self):
		super(CustSignal, self).__init__()
		self.setWindowTitle('Customized Singal and Slot function sample')
		self.resize(200,100)

		btn = QPushButton('click',self)
		btn.clicked.connect(self.emitSignal)
		self.signal.connect(self.getValue)
	def emitSignal(self):
		self.signal.emit(1000)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	custsigal = CustSignal()

	custsigal.show()
	sys.exit(app.exec())






		
