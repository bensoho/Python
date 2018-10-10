#ex40.py
# things = ['a','b','c','d']
# print(things[1])
# things[1] = 'z'
# print(things)
# stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
# print(stuff['age'])
# stuff['height'] = 180

# stuff['city'] = 'shenzhen'

# print(stuff)

# stuff[1] = 'benjamin'
# stuff[2] = 'liu'
# print(stuff[1])

# print(stuff)

# del stuff[1]
# del stuff[2]
# print(stuff)
cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return 'Not Found.'

# Pay attention!
# cities['_find'] = find_city

for k,v in cities.items():
	print(k + ' = ' + v)


while True:


	print("State> (ENTER to quit)", end = " ")
	state = input('> ')
	if not state: break


	#this line is the most imortant ever! study!

	city_found = find_city(cities,state)
	print(city_found)


