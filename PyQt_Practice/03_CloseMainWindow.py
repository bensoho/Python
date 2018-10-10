#CloseMainWindow.py
from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget
import sys

class WinForm(QMainWindow):
	"""docstring for WinForm"""
	def __init__(self, parent=None):
		super(WinForm, self).__init__(parent)
		self.setWindowTitle("CloseMainWindow")	#set window title
		self.resize(400,200)					#set window size
		self.setFixedWidth(400)	#fixed width
		self.setFixedHeight(200)	#fixed height
		self.button1 = QPushButton("CloseMainWindow")	#create button with button title
		self.button1.clicked.connect(self.onButtonClick)	#setup connection with slot after clicked

		layout = QHBoxLayout()	#create a horizontal layout object
		layout.addWidget(self.button1)	#add widget 'button1' into the layout object

		main_frame = QWidget()	#create a widget object
		main_frame.setLayout(layout)	#set object layout into QWidget object
		self.setCentralWidget(main_frame)	#set to show in center

	def onButtonClick(self):
		#sender is the object of sending signal
		sender = self.sender()
		print(sender.text() + ' pushed')
		Qapp = QApplication.instance()
		Qapp.quit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()

	print(form.size())

	print(form.width(),form.height())
	print(form.x(),form.y())
	print(form.geometry())
	print(form.frameGeometry())	#get window height,width
	form.move(10,10)
	print(form.pos())

	sys.exit(app.exec_())

