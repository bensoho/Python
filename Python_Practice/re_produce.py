#re_produce
class RoundFloat(float):
	def __new__(cls,val):
		return super(RoundFloat,cls).__new__(cls,round(val,2))

class SortedKeyDict(dict):
	def keys1(self):
		return sorted(super(SortedKeyDict,self).keys())


d = {'zhengcai':67,'huijun':68,'xin-yi':2}

s = SortedKeyDict(d)

print(s.keys1())


