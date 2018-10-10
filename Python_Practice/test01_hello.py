def greeting(name):
	print('hello,{}'.format(name))

greeting("Andy")


class Person(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

class Student(Person):
	"""docstring for Student"""
	def __init__(self, name, age,score):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.score = score
		