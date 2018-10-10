#anyIter.py

class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe=safe
        self.iter=iter(data)

    def __iter__(self):
        return self


    def next(self,howmany=1):
        retval=[]
        for eachItem in range(howmany):
            try:
                retval.append(next(self.iter))
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

a = AnyIter(range(10),True)
i = a.iter

print(a.next(14))

# for j in range(1,5):
#     print(j,':',a.next(j))







	






