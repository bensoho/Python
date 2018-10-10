#WidgetGeometry.py
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

def btnClose(self):
	sender = self.sender()
	qt = QApplication.instance()
	qt.quit()


app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("WidgetGeometry")


btn = QPushButton(widget)
btn.setText("benjamin")
btn.move(10,10)
widget.resize(300,200)
widget.move(100,200)
widget.show()

btn.clicked.connect(btnClose)

sys.exit(app.exec_())