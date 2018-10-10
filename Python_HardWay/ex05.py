#ex05.py
#coding:utf-8
name = 'Benjamin Liu'
age = 30
height = 173 #cm
weight = 64 # kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print("Let's talk about %s." % name)
print("He's %scm tall." % height)
print("He's %skgs heavy." % weight)
print('Actually that is not too heavy.')
print("He's got %s eyes and %s teeth and %s hair" % (eyes,teeth,hair))
print("If I add %d, %d and %d I get %d. " %(age,height,weight,age+height+weight))
print("他的名字叫%r"%name)
print("His name is %s."%(name))
print("His name is %r."%(name))

import datetime
d = datetime.date.today()
print('%s'%d)
print('%r'%d)

