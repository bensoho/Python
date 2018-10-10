class Fib(object):

    def __init__(self, num):
        self.num = num

    def __str__(self):
        L = [0,1]
        for x in range(0,self.num - 2):
            L.append(L[-2]+L[-1])
        return str(L)

    def __len__(self):
        return self.num

f = Fib(10)
print f
print len(f)