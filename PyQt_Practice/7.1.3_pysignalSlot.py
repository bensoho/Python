#7.1.3_pysignalSlot.py
from PyQt5.QtCore import QObject, pyqtSignal
class QTypeSignal(QObject):
	"""docstring for QtypeSignal"""
	sendmsg = pyqtSignal(object,object)
	def __init__(self):
		super(QTypeSignal, self).__init__()
		
	def run(self):
		self.sendmsg.emit('hello PyQt5!',' How are you?')

class QTypeSlot(QObject):
	"""docstring for QTypeSlot"""
	def __init__(self):
		super(QTypeSlot, self).__init__()
	def get(self,msg1,msg2):
		print("QSlot get mesg=>"+msg1 + msg2)

if __name__ == "__main__":
	send = QTypeSignal()
	slot = QTypeSlot()

	print('bind the signal to slot function')
	send.sendmsg.connect(slot.get)
	send.run()

	print('disconnect the signal with slot')
	send.sendmsg.disconnect(slot.get)
	send.run()
