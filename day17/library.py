from data import*


def print_report(resources, profit):
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${profit}")

def drink(choice):
	if choice in MENU:
		print("existe")
	else:
		print("não existe")
