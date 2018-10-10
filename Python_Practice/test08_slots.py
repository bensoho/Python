class Student(object):
	"""docstring for Student"""
	__slots__ = ('name', 'gender', 'score')
	def __init__(self, name, gender, score):
		self.name = name
		self.gender = gender
		self.score = score
		
s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
#s.grade = 'A'