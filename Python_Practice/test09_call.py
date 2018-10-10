# #test09_call.py
# class Person(object):
# 	"""docstring for Person"""
# 	def __init__(self, name,gender):
# 		super(Person, self).__init__()
# 		self.name = name
# 		self.gender = gender
# 	def __call__(self, friend):
# 		print 'My name is %s ...' % self.name
# 		print 'My friend is %s ...' % friend

# p = Person('Bob', 'male')
# p('Tim')
# print(type(p))

class Fib(object):
	def __call__(self,num):
		L = [0,1]
		for x in range(0,num-2):
			L.append(L[-2] + L[-1])
		return L


f = Fib()
print f(3)