from coffee_data import MENU, resources
from time import sleep


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


# TODO check transaction successful
def transaction(total, cost):
	print(f"this is the total again: {total}")
	print(f"this is the cost again: {cost}")
	if cost == total:
		print("That's perfect, no change given")
	elif total > cost:
		change = round(total - cost, 2)
		print(f"That's enough, here is some change {change}")
	else:
		print("Not enough coins.")


print("-----MENU-----")
for coffee in MENU:
	print(f"{coffee}: ${MENU[coffee]["cost"]}0")

order = input(f"What would you like: ")

# TODO check resources
if order == "report":
	print("Generating report...")
	sleep(2)
	report()
# TODO turn off machine
if order == "off":
	print("Machine is turning off...")
	sleep(2)
	exit()
if order in MENU:
	print(f"That'll be ${MENU[order]["cost"]}0 ")
	cost = MENU[order]["cost"]
	print("please insert coins.")
	transaction(coin_machine(), cost)

# TODO make coffee
