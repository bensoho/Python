#!/usr/bin/env python3
#ex03_tuple.py
records = [
('foo',1,2),
('bar','hello'),
('foo',3,4),
]

def do_foo(x,y):
	print('foo',x,y)

def do_bar(s):
	print('bar',s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)


line = 'nobody:*:-2:-2:Unpriviledged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
print(uname)

print(homedir)
print(sh)

