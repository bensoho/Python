#11_QTableView.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Table(QWidget):
	"""docstring for Table"""
	def __init__(self, parent=None):
		super(Table, self).__init__()
		self.setWindowTitle("QTableView Sample")
		self.resize(500,300)
		self.model = QStandardItemModel(4,4)
		self.model.setHorizontalHeaderLabels(['Title1','Title2','Title3','Title4'])

		for row in range(4):
			for column in range(4):
				item = QStandardItem('row %s,column %s'%(row,column))
				self.model.setItem(row,column,item)

		self.tableView = QTableView()
		self.tableView.setModel(self.model)
		#fill and resize the tableview
		self.tableView.horizontalHeader().setStretchLastSection(True)
		self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


		dlgLayout = QVBoxLayout()
		dlgLayout.addWidget(self.tableView)
		self.setLayout(dlgLayout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	table = Table()
	table.show()
	#add new row
	table.model.appendRow([
		QStandardItem('row %s,column %s'%(11,11)),
		QStandardItem('row %s,column %s'%(11,12)),
		QStandardItem('row %s,column %s'%(11,13)),
		QStandardItem('row %s,column %s'%(11,14))
		])
	sys.exit(app.exec_())

