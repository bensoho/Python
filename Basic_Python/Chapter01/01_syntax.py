# -*- coding: utf-8 -*-
# 标识符

# 第一个字符必须是字母表中字母或下划线'_'。
# 标识符的其他的部分有字母、数字和下划线组成。
# 标识符对大小写敏感。
# python保留字

# 保留字即关键字，我们不能把它们用作任何标识符名称。
# Python的标准库提供了一个keyword module，可以输出当前版本的所有关键字
import keyword
print(keyword.kwlist)

# 注释

# Python中单行注释以#开头，多行注释用三个单引号（'''）或者三个双引号（"""）将注释括起来。

#自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
str = r'''
this is multi-line
also you can use \''' or \"""
to show the multi-line contents.
'''

print(str)

str1 = u"this is an unicode string."

print(str1)