import random

class Die:

	def __init__(self, sides = 6, value = 1):

		self._value = value
		self._sides = sides
		self._random = random
	
	def Value(self):
		return self._value
    
	def Sides(self):
		return self._sides
    
	def Roll(self):
    
		self._value = self._random.randint(1, self._sides)
		return self._value
    
	def __lt__ (self, other):
		return self.Value < other.Value

	def __str__(self):
		return str(self._value)
    

