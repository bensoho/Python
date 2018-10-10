#heritage.py
class P(object):
	'P class'
	def __init__(self):

		print("Good, created an object of ",self.__class__.__name__)

	def foo(self):
		print("Hi, I am P - foo()")


class C(P):
	def __init__(self):
		super(C,self).__init__()
		#print("created an object of ",self.__class__.__name__)
	def foo(self):
		super(C,self).foo()
		print("Hi, I am C - foo()")


c = C()
c.foo()


