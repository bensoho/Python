#ex18.py
#习题 18: 命名、变量、代码、函数
#this one is like your scripts with argv

def print_two(*args):
	arg1,arg2 = args
	print("arg1: %r, arg2: %r" % (arg1,arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print("arg1: %r, arg2: %r" % (arg1,arg2))

# this just takes only one argument
def print_one(arg1):
	print("arg1: %r" % arg1)

def print_none():
	print("I got no argument")


print_two("Ben","Liu")
print_two_again("SHEING","HAI")
print_one("benjaminliu")
print_none()