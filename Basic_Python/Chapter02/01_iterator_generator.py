# 迭代器

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：
import sys

# list = [1,2,3,4]
# it = iter(list)

# # for x in it:
# #     print(x,end = " ")

# while True:
#     try:
#         print(next(it),end=" ")
#     except StopIteration:
#         sys.exit()

# 生成器

# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)


for x in f:
    print(x, end = " ")
#每次遇到yield时函数暂停，这时用迭代器可以显示yield产生的值,yield
#必须跟for循环的迭代器一起使用

