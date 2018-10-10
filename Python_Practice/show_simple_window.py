#show_simple_window.py
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.resize(400,200)
		self.status = self.statusBar()
		self.status.showMessage("This is status alert",2000)
		self.setWindowTitle("PyQt sample")
		#self.setGeometry(400,200,200,200)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())




