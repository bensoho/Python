# Python3 字典

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
# d = {key1 : value1, key2 : value2 }
# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dict['Jim'] = '1000'
# dict['School'] = 'W3C Course'
# print(dict)
# print(dict['Jim'],dict['Cecil'],dict['School'])

# del dict['Alice']
# print(dict)

# del dict
# # dict.clear()
# print(dict)

# 字典键的特性

# 字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

dict = {'Age': 7, 'Name': '小菜鸟'}

# print ("dict['Name']: ", dict['Name'])
#2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# 字典内置函数&方法

# Python字典包含了以下内置函数：
#len(dict), str(dict), type(dict)
#Python字典包含了以下内置方法：
#clear(),copy(),fromkeys(),key in dict, items(), keys(),
#values(),setdefault(key,default=None),update(dict2)
print(list(dict.values()))