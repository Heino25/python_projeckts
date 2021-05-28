# #8-1
# def display_message(username):
# 	print(f"\nHello my name is {username.title()}, and I'll be learning about chapter 8")

# display_message('Heino')

#8-3
# def make_shirt(shirt_size, shirt_saying):
# 	##disply information of shirt
# 	print(f"\nMy shirt size is {shirt_size}.")
# 	print(f"\nSaying {shirt_saying}.")

# make_shirt('"Large"', '"Cool shirt"')

#8-10
def short_messages(messages):
	"""Print a simple messagein the list."""
	for message in messages:
		msg = f"The short message is {message.title()}."
		print(msg)

themessages = ['have a good day', 'have a great day', 'have a wonderful day']
short_messages(themessages)