#创建主窗口QMainWindow.py
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.resize(400,200)
		self.status = self.statusBar()
		self.status.showMessage("This is status bar alert!",5000)
		self.setWindowTitle("MainWindow Sample")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())
