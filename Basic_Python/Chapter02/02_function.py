# def hello():
#     print('Hello, world!')

# hello()

# def sayhi(name, age):
#     print('my name is {}, {} years old.'.format(name,age))

# sayhi('benjamin',20)

# 函数变量作用域

# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

# a = 4
# def my_function1():
#     a = 17
#     print('in my_function1 a = ',a)

# def my_function2():
#     print('in my_function2 a = ',a)

# my_function1()
# my_function2()
# print(a)

# 关键字参数

# 函数也可以使用 kwarg=value 的关键字参数形式被调用.例如,以下函数
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot('a million', 'bereft of life', 'jump')

# 返回值

# Python的函数的返回值使用return语句，可以将函数作为一个值赋值给指定变量：
# def return_sum(x,y):
#     c = x + y
#     return c

# res = return_sum(4,5)
# print(res)

# 可变参数列表

# 最后,一个最不常用的选择是可以让函数调用可变个数的参数.这些参数被包装进一个元组(查看元组和序列).在这些可变个数的参数之前,可以有零到多个普通的参数:

def arithmetic_mean(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(45))