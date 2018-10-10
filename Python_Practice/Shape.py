#Shape.py
import math
class Point(object):
	"""docstring for Point"""
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return math.hypot(self.x,self.y)

	def __repr__(self):
		return 'Point({0.x!r},{0.y!r})'.format(self)

	def __str__(self):
		return '({0.x!r},{0.y!r})'.format(self)

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y


class Circle(Point):
	def __init__(self,radius,x=0,y=0):
		super(Circle,self).__init__(x,y)
		self.radius = radius

	@property
	def radius(self):
		return self.__radius
	@radius.setter
	def radius(self,radius):
		assert radius > 0, 'radius must be nonzero and non-negative.'
		self.__radius = radius

	@property
	def edge_distance_from_origin(self):
		return abs(self.distance_from_origin()-self.radius)

	@property
	def area(self):
		return math.pi * (self.radius**2)

	def cirle_length(self):
		return math.pi*2*(self.radius)

	def __eq__(self,other):
		return self.radius == other.radius and super().__eq__(other)

	def __repr__(self):
		return 'Circle{0.radius!r},{0.x!r},{0.y!r}'.format(self)

	def __str__(self):
		return repr(self)

c = Circle(3,4)
c.radius = 50
print(c.radius)





