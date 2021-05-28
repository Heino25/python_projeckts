# #7-1
# prompt = "What rental car would you like?"
# name = input(prompt)
# print(f"\nLet me see if I can find you a {name}!")

#7-2
# people = input("How many people do you want to reserve a table for?")
# people = int(people)

# if people <= 8:
# 	print("\n Reservation made.")
# else:
# 	print("\n No Room for reservation")

# #7-3
# number = input("Enter a number, and I'll tell you if it's multiples of 10: ")
# number = int(number)
# if number % 10 == 0:
# 	print(f"\n{number} is a multiple of 10.")
# else:
# 	print(f"\n{number} is not a multiple of 10.")

##7-8
# # Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches

sandwich_orders = ['tuna', 'chicken', 'cheese']
finished_sandwiches = []

# Make a list called sandwich_orders and fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(F"Verifying order: {current_sandwich.title()}")
	finished_sandwiches.append(current_sandwich)

# Display all confirmed users.
print("\nThe following orders have been confirmed:")
for finished_sandwiches in finished_sandwiches:
	print(finished_sandwiches.title())

people_orders = {
'jen': 'chicken',
'sarah': 'cheese',
'edward': 'tuna',
}

friends = ['jen', 'sarah', 'edward']
for name in people_orders.keys():
	print(name.title())

	if name in friends:
		order = people_orders[name].title()
		print(f"\t{name.title()}, I see you love {order}!")