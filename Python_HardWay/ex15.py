#ex15.py
#习题 15: 读取文件
'''
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
'''
from sys import argv
script, filename = argv
txt = open(filename)
print("Here's your file %r:" % filename)
print(txt.read())
txt.close()
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()