#os.path_os.py
import os,sys
for tmpdir in ('/Users/benjaminliu/File',r'c:\temp'):
 	if os.path.isdir(tmpdir):	#if tmpdir exist and is a directory
 		break
 	else:
 		print('no temp directory available')
 		tmpdir = ''
 		print(bool(tmpdir))

#print(sys.argv)

if tmpdir:
	os.chdir(tmpdir)	#change current directory
	cwd = os.getcwd() #return to current directory
	print('***current temporary directory')
	print(cwd)

	print('***creating example directory...')
	os.mkdir('example')
	os.chdir('example')
	cwd = os.getcwd()
	print('***new working directory: ')
	print(cwd)
	print('***original directory listing: ')
	print(os.listdir(cwd))
	print('creating test file...')
	fobj = open('test','w')
	fobj.write('foo\n')
	fobj.write('bar\n')
	fobj.close()
	print('***updated directory listing: ')
	print(os.listdir(cwd))

	print("renaming 'test' to 'filetest.txt'")
	os.rename('test','filetest.txt')
	print('***updated directory listing: ')
	print(os.listdir(cwd))
	

