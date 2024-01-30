from coffee_data import MENU, resources
from time import sleep

ordering = True

# TODO print report
def report():
	for ingredient, values in resources.items():
		print(f"{ingredient} : {values}")


# TODO process coins
def coin_machine():
	quarters = int(input("How many quarters?: "))
	dimes = int(input("How many dimes?: "))
	nickles = int(input("How many nickles?: "))
	pennies = int(input("How many pennies?: "))
	total = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
	return total

def update_money(total):
	old_total = resources.get("Money")
	total = old_total + total
	resources["Money"] = total
	return total

# TODO check transaction successful
def transaction(total, cost):
	print(f"this is the total again: {total}")
	print(f"this is the cost again: {cost}")
	if cost == total:
		update_money(cost)
		print("That's perfect, no change given")
	elif total > cost:
		update_money(cost)
		change = round(total - cost, 2)
		print(f"Thank you, here is your change {change}")
	else:
		print("Not enough coins.")


while ordering != False:
	print("-----MENU-----")
	for coffee in MENU:
		print(f"{coffee}: ${MENU[coffee]["cost"]}0")

	order = input(f"What would you like: ")

	machine_water = resources["water"]
	order_water = MENU[order]["ingredients"]["water"]

	# TODO work on this. Checking if milk is in the ingredients list
	# if MENU[order]["ingredients"]["milk"] in MENU[order]["ingredients"]:
	# 	machine_milk = resources["milk"]
	# 	order_milk = MENU[order]["ingredients"]["milk"]

	machine_coffee = resources["coffee"]
	order_coffee = MENU[order]["ingredients"]["coffee"]

	# TODO check resources
	if order == "report":
		print("Generating report...")
		sleep(2)
		report()
	# TODO turn off machine
	if order == "off":
		print("Machine is turning off...")
		sleep(2)
		ordering = False
		exit()
	if order in MENU:
		if machine_water >= order_water or machine_milk >= order_milk or machine_coffee >= order_coffee:

			new_water = machine_water - order_water
			new_milk = machine_milk - order_milk
			new_coffee = machine_coffee - order_coffee

			resources["coffee"] = new_coffee
			resources["milk"] = new_milk
			resources["water"] = new_water

			print(f"That'll be ${MENU[order]["cost"]}0 ")
			cost = MENU[order]["cost"]
			print("please insert coins.")
			transaction(coin_machine(), cost)
		else:
			print("Not enough resources.")

# TODO make coffee
