#static method
class TestStaticMethod:
	@staticmethod
	def foo():
		print("calling static method foo()")


class TestClassMethod:
	@classmethod
	def foo(cls):
		print("calling class method foo()")
		print("foo() is part of class:",cls.__name__)

TestStaticMethod.foo()
tst = TestClassMethod()
tst.foo()

