from calc_art import logo


def add(first_num, sec_num):
	return first_num + sec_num


def subtract(first_num, sec_num):
	return first_num - sec_num


def multiply(first_num, sec_num):
	return first_num * sec_num


def divide(first_num, sec_num):
	return first_num / sec_num


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}


def calculator():
	print(logo)
	first_num = float(input("Enter first number: "))
	for symbol in operations:
		print(symbol)
	mathing = True

	while mathing:
		operation_symbol = input("Pick an operation from the line above: ")
		sec_num = float(input("Enter next number: "))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(first_num, sec_num)

		print(f"{first_num} {operation_symbol} {sec_num} = {answer}")

		if input(f"Do you want to continue with the last answer: {answer}? (y or no) or type 'n' to restart") == "y":
			first_num = answer
		else:
			print("restarting...")
			mathing = False
			calculator()


calculator()
