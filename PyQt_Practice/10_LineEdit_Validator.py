#10_LineEdit_Validator.py
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class LineEditDemo(QWidget):
	"""docstring for LineEditDemo"""
	def __init__(self, parent=None):
		super(LineEditDemo, self).__init__(parent)
		self.setWindowTitle('QLineEdit Validator sample')

		flo = QFormLayout()
		pIntLineEdit = QLineEdit()
		pDoubleLineEdit = QLineEdit()
		pValidatorLineEdit = QLineEdit()

		flo.addRow('Integer',pIntLineEdit)
		flo.addRow('Float',pDoubleLineEdit)
		flo.addRow('Letter and number',pValidatorLineEdit)

		pIntLineEdit.setPlaceholderText('Integer')
		pDoubleLineEdit.setPlaceholderText('Float')
		pValidatorLineEdit.setPlaceholderText('Letter and number')

		pIntValidator = QIntValidator(self)
		pIntValidator.setRange(1,99)

		pDoubleValidator = QDoubleValidator(self)
		pDoubleValidator.setRange(-100,100)
		pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
		pDoubleValidator.setDecimals(2)

		reg = QRegExp("[a-zA-Z0-9]+$")
		pValidator = QRegExpValidator(self)
		pValidator.setRegExp(reg)


		pIntLineEdit.setValidator(pIntValidator)
		pDoubleLineEdit.setValidator(pDoubleValidator)
		pValidatorLineEdit.setValidator(pValidator)


		self.setLayout(flo)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	demo = LineEditDemo()
	demo.show()
	sys.exit(app.exec_())


		

