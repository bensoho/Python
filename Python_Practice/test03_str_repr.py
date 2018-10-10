#--coding:utf-8--
#请给Student 类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__

class Student(Person):
	"""docstring for Student"""
	def __init__(self, name,gender,score):
		super(Student, self).__init__(name,gender)
		self.score = score

	def __str__(self):
		return '(Student: %s, %s, %s)' % (self.name,self.gender,self.score)


s = Student('bob','male',89)
print(s)