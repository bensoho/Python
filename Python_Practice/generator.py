#generator.py
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
L = [x * x for x in range(10)]
# print(L)

#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x*x for x in range(10))
# print(g)
#<generator object <genexpr> at 0x1038a70a0>
# for n in g:
# 	print(n)

#著名的斐波拉契数列（Fibonacci）

def fib(max):
	n,a,b = 0,0,1
	while n < max:
		# print(b,end=' ')
		yield b
		a,b=b,a+b
		n += 1
	return 'done'
f = fib(6)
print(f)

for n in f:
	print('g:',n)
