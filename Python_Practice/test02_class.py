class Programer(object):
	hobby = 'Play computer'

	def __init__(self,name,age,weight):
		self.name=name
		self._age=age
		self.__weight=weight

	@classmethod
	def get_hobby(cls):
		return cls.hobby

	@property
	def get_weight(self):
		return self.__weight

	def self_introduction(self):
		print('My name is %s \nI am %s years old\n' % (self.name,self._age))

p = Programer('Bob',19,60)
print(p.hobby)
print(p.name)
print(p._age)
print(Programer.get_hobby())
print p.get_weight
p.self_introduction()