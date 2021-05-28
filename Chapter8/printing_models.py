def print_models(unprinted_designs, completed_models):
	"""
Simulate printing each design, until none are left.
Move each design to completed_models after printing.
"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print(f"\nThe following models have been printed:")
	for completed_models in completed_models:
		print(completed_models)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)