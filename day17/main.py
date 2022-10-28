from data import resources 


def print_report( ):
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
#	print(f"Money: ${profit}")

is_on = True

while is_on:
	choice = input("What would you like? (espresso/latte/cappuccino):")
	if choice == "off":
		is_on = False
	elif choice == "report":
		print_report( )



