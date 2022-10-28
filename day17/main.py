from data import*
from library import*



is_on = True

while is_on:
	choice = input("What would you like? (espresso/latte/cappuccino):")
	if choice == "off":
		is_on = False
	elif choice == "report":
		print_report(resources, profit)
	else:
		drink(choice)



