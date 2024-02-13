from coffee_data import MENU, resources
from time import sleep

ordering = True

def report():
	for ingredient, values in resources.items():
		print(f"{ingredient} : {values}")

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

def check_resources(coffee):
	# check if milk is in order and have enough
	if "milk" in MENU[coffee]["ingredients"]:
		if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
			print("Not enough milk, order something else")
			return False
		else:
			resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]

	# check if water ''''''
	if "water" in MENU[coffee]["ingredients"]:
		if MENU[coffee]["ingredients"]["water"] > resources["water"]:
			print("Not enough water, order something else.")
			return False
		else:
			resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]

	# check if coffee '''
	if "coffee" in MENU[coffee]["ingredients"]:
		if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
			print("Not enough coffee, order something else")
			return False
		else:
			resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
	return resources


while ordering != False:
	print("-----MENU-----")
	for coffee in MENU:
		print(f"{coffee}: ${MENU[coffee]["cost"]}0")

	order = input(f"What would you like: ")

	if order == "report":
		print("Generating report...")
		sleep(2)
		report()

	if order == "off":
		print("Machine is turning off...")
		sleep(2)
		ordering = False
		exit()
	if order in MENU:
		if check_resources(order) != False:
			print(f"That'll be ${MENU[order]["cost"]}0 ")
			cost = MENU[order]["cost"]
			print("please insert coins.")
			transaction(coin_machine(), cost)