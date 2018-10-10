#numstr.py
#!usr/bin/env python3
class NumStr(object):
	"""docstring for NumStr"""
	def __init__(self, num=0, string=''):
		self.__num = num
		self.__string = string
		
	def __str__(self):
		return '[{0}::{1!r}]'.format(self.__num,self.__string)
	__repr__ = __str__

	def __add__(self,other):
		if isinstance(other, NumStr):
			return self.__class__(self.__num+other.__num,self.__string+other.__string)
		else:
			raise TypeError('Illegal argument type for built-in operation')


	def __mul__(self,num):
		if isinstance(num,int):
			return self.__class__(self.__num * num,self.__string*num)
		else:
			raise TypeError('Illegal argument type for built-in operation')

	def __bool__(self):
		return bool(self.__num or len(self.__string))

	def __gt__(self,other):
		return self.__num >= other.__num and self.__string >= other.__string
	def __lt__(self,other):
		return self.__num <= other.__num and self.__string <= other.__string		
	def __eq__(self,other):
		return self.__num == other.__num and self.__string == other.__string



exec_code = compile("""
req = input('Count how many numbers? ')
for eachNum in range(int(req)):
	print(eachNum)""",'','exec')

exec(exec_code)



