#7.1.3_winSignalSlot01.py
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget,QMessageBox
import sys

app = QApplication(sys.argv)
widget = QWidget()

def showMsg():
	QMessageBox.information(widget,"Message alert","OK, jump off info.")

btn = QPushButton('Test button',widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())
