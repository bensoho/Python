#ex13.py
#习题 13: 参数、解包、变量

from sys import argv



script, first, second, third = argv

first = input("Enter your name: ")
second = input("Enter your age: ")
third = input("Enter your height: ")

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is",second)
print("Your third variable is",third)
