#multi-process.py
import os

#print('Process {} start...'.format(os.getpid()))
#only works on Unix/Linux/Mac
pid = os.fork()	#system call function

print('child ID:',pid)
if pid == 0:
	print('I am child process ({0}) and my parent is {1}.'.format(os.getpid(),os.getppid()))
else:
	print('I ({0}) just created a child process {1}.'.format(os.getpid(),pid))
	print('Now the child pid is {}.'.format(pid))
