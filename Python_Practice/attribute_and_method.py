#attribute_and_method.py
class RoundFloatManual(object):
	def __init__(self,val):
		assert isinstance(val,float), 'Value must be a float!'

		self.value = round(val,2)


	def __str__(self):
		return "{0:.2f}".format(self.value)
	__repr__ = __str__

print(RoundFloatManual(888883.598))

