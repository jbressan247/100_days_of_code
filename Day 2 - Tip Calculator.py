print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill?\n"))
num_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("How much would you like to tip? | 10% | 15% | 20% |\n"))

tip_dollar = total_bill * (tip_percentage/100)

per_person = round(((total_bill + tip_dollar)/num_people), 2)

per_person_format = "{:.2f}".format(per_person)

print(f"Each person should pay: ${per_person_format}")