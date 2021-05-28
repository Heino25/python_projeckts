class Dog:
	""" A simple atempt to model a dog."""
	def __init__(self, name, age, breed=''):
		"""Initialize name, age and breed attributes."""
		self.name = name
		self.age = age
		self.breed = breed

	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate roll over in response to a command """
		print(F"{self.name} Rolled over!")

# my_dog = Dog('Willie', 3, 'Pitbull')
your_dog = Dog('Lucy', 6, 'pugg')

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# print(f"My dog is a {my_dog.breed}.")

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
print(f"Your dog is a {your_dog.breed}.")

# my_dog.sit()
# my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()