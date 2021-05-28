class Restuarant:
	""" A Simple attempt to make a restuarant"""
	def __init__(self, restuarant_name, cuisine_type):
		"""Initialize attributes."""
		self.restuarant_name = restuarant_name
		self.cuisine_type = cuisine_type


	def describe_restuarant(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.restuarant_name} is a type of {self.cuisine_type} Restuarant."
		return long_name.title()

	def open_restuarant(self):
		print(f"{self.restuarant_name} is now open.")

my_restuarant = Restuarant('Rio Sol', 'sea food')
print(my_restuarant.describe_restuarant())

my_restuarant = Restuarant()
print(my_restuarant.open_restuarant())