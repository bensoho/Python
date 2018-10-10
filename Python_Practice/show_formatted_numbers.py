#show_formatted_numbers.py

class Time60(object):
	def __init__(self,hr,min):
		self.hour = hr
		self.minute = min

	def __str__(self):
		if self.minute < 10:
			mm = "0" + str(self.minute)
			return "{0:d}:{1:s}".format(self.hour,mm)
		return "{0:d}:{1:d}".format(self.hour,self.minute)

	__repr__ =  __str__


	def __add__(self,other):

		if self.minute + other.minute >= 60:
			tm = self.minute + other.minute - 60
			th = self.hour + other.hour + 1
		else:
			tm = self.minute + other.minute
			th = self.hour + other.hour

		return self.__class__(th,tm)



	def __iadd__(self,other):
		self.hour += other.hour
		self.minute += other.minute
		if self.minute >= 60:
			tm = self.minute - 60
			th = self.hour + 1
		else:
			tm = self.minute
			th = self.hour

		return self.__class__(th,tm)


mon = Time60(10,50)
tue = Time60(11,45)

mon += tue
print(mon)

