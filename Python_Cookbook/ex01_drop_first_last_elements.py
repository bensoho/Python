#ex01_drop_first_last_elements.py

def drop_first_last(grades):
	first, *middle, last = grades
	return middle

g = [12,45,89,100,78,34,99,57,76]

s = drop_first_last(g)
print(s)
