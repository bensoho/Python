#07_QLabel.py
from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class WindowDemo(QWidget):
	"""docstring for WindowDemo"""
	def __init__(self,parent=None):
		super(WindowDemo, self).__init__(parent)

		label1 = QLabel(self)
		label2 = QLabel(self)
		label3 = QLabel(self)
		label4 = QLabel(self)

		label1.setText("This is text label.")
		label1.setAutoFillBackground(True)

		label1.setAlignment(Qt.AlignCenter)
		palette = QPalette()
		palette.setColor(QPalette.Window,Qt.yellow)
		label1.setPalette(palette)
		label1.setAlignment(Qt.AlignCenter)

		label2.setText("<a href='#'>welcome to use python GUI </a>")
		label2.setAutoFillBackground(True)
		palette2 = QPalette()
		palette2.setColor(QPalette.Window,Qt.red)
		label2.setPalette(palette2)

		label3.setAlignment(Qt.AlignCenter)
		label3.setToolTip('This is picture label')
		label3.setPixmap(QPixmap("img/book.ico"))

		label4.setText("<a href='http://www.cnblogs.com/wangshuo1'>welcome to my house</a>")
		label4.setAlignment(Qt.AlignRight)
		label4.setToolTip("This is hyper link")



		vbox = QVBoxLayout()
		vbox.addWidget(label1)
		vbox.addStretch()
		vbox.addWidget(label2)
		vbox.addStretch()
		vbox.addWidget(label3)
		vbox.addStretch()
		vbox.addWidget(label4)

		label1.setOpenExternalLinks(True)
		label4.setOpenExternalLinks(True)

		label4.linkActivated.connect(link_clicked)
		label2.linkHovered.connect(link_hovered)
		label1.setTextInteractionFlags(Qt.TextSelectableByMouse)


		self.setLayout(vbox)
		self.setWindowTitle("Label sample")

def link_clicked():
	print("when mouse click label4, trigger an event")
def link_hovered():
	print("when mouse moved to label2, trigger an event")





if __name__=="__main__":
	app = QApplication(sys.argv)
	win = WindowDemo()
	win.show()
	sys.exit(app.exec_())