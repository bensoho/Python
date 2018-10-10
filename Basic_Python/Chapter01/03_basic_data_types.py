#Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

# Python 3中有六个标准的数据类型：
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionaries（字典）

# Numbers（数字）

# Python 3支持int、float、bool、complex（复数）。
# 数值类型的赋值和计算都是很直观的，就像大多数语言一样。内置的type()函数可以用来查询变量所指的对象类型。

# a, b, c, d = 20, 5.5, True, 4 + 3j
# print(type(a), type(b), type(c), type(d))

# # 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# # 2、一个变量可以通过赋值指向不同类型的对象。
# # 3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
# # 4、在混合计算时，Pyhton会把整型转换成为浮点数。

# print(20//4)

# # String（字符串）

# # Python中的字符串str用单引号(' ')或双引号(" ")括起来，同时使用反斜杠(\)转义特殊字符。
# s = 'Yes, He doesn\'t'
# print(s,type(s),len(s))

#如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串：

# print('C:\some\name')
# print(r'C:\some\name')

# # 另外，反斜杠可以作为续行符，表示下一行是上一行的延续。还可以使用"""..."""或者'''...'''跨越多行。
# # 字符串可以使用 + 运算符串连接在一起，或者用 * 运算符重复：

# print('this is \
# another line')

# print('str' + 'ing', 'my'*5)

# word = 'Python'
# print(word[0], word[5])

# print(word[-1], word[-6])

# print(word[0:4])

# print(word[-1:-5])
# 与C字符串不同的是，Python字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。

# List（列表）

# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表是写在方括号之间、用逗号分隔开的元素列表。列表中元素的类型可以不相同：

# a = ['him', 25, 100,'her']
# print(a[0:2])
# # 和字符串一样，列表同样可以被索引和切片，列表被切片后返回一个包含所需元素的新列表。详细的在这里就不赘述了。
# # 列表还支持串联操作，使用+操作符：
# print(a+[6,7,8])

#与Python字符串不一样的是，列表中的元素是可以改变的：
# a = [1, 2, 3, 4, 5, 6]
# a[0] = 9
# a[2:5] = [13,14,15]
# print(a)
# a[2:5] = []
# print(a)
# # List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
# # 注意：
# # 1、List写在方括号之间，元素用逗号隔开。
# # 2、和字符串一样，list可以被索引和切片。
# # 3、List可以使用+操作符进行拼接。
# # 4、List中的元素是可以改变的。

# Tuple（元组）

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。

# tup1 = (2,3)
# tup2 = (1,7)
# print(tup1 + tup2)
# # 注意：
# # 1、与字符串一样，元组的元素不能修改。
# # 2、元组也可以被索引和切片，方法一样。
# # 3、注意构造包含0或1个元素的元组的特殊语法规则。
# # 4、元组也可以使用+操作符进行拼接。
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)
# print('Tom' in student)

# Dictionaries（字典）

# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。

# dic = {}
# tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
# print(tel)
# print(tel['Tom'])
# del tel['Rose']
# print(tel)
# tel['Ben'] = 234040
# print(tel)
# print(list(tel.keys()))
# print(list(tel.values()))
# print(sorted(tel.keys()))
# print('Mary' not in tel)

# lst = [('sape', 4139), ('guido', 4127), ('jack', 4098)]
# print(dict(lst))

# print({x:x**2 for x in range(5)})

