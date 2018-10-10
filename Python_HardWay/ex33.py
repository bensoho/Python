#ex33.py

def while_loop(n):
	i = 0
	numbers = []


	while i < n:
		#print("At the top i is %d" % i)
		numbers.append(i)

		i+=1
		print("Numbers now: ", numbers)
		#print("At the bottom i is %d" % i)
	return numbers



for num in while_loop(20):
	print(num)
