class Students(object):
	"""docstring for Students"""
	def __init__(self, *args):
		super(Students, self).__init__()
		self.names = args
		
	def __len__(self):
		return len(self.names)

ss = Students('Bob','Alice','Tim')
print(len(ss))