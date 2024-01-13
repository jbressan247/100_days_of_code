import random
import string


def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters  # assigning the variable the letters from import string
    digits = string.digits  # assigning the variable the digits from import string
    special = string.punctuation  # assigning the variable the special character from import string

    characters = letters  # by default includes letters from the import string
    if numbers:  # if numbers is True, add numbers from import string in the characters string
        characters += digits
    if special_character:  # if special_character is True, add special_character from import string in the characters string
        characters += special
    pwd = ""  # empty variable to add the characters to
    meets_criteria = False  # variable to check if the password meets the criteria
    has_number = False  # variable to check if password has number
    has_special = False  # variable to check if password has special character

    # main program, picks a random character from the characters string and adds to pwd variable
    while not meets_criteria or len(
            pwd) < min_length:  # loops while meets_criteria is False or while  length of  password is less than min_length
        new_char = random.choice(
            characters)  # pick a random character from characters and assigns it the new_char variable
        pwd += new_char  # adds the new_char to the pwd variable

        if new_char in digits:  # checks if the new_char is a digit
            has_number = True  # if new char is a digit, set has_number to True
        elif new_char in special:  # checks if new_char is a special character
            has_special = True  # if new_char is a special character, set has_special to True

        # a reverse check, set meets criteria to true and see if it is set back to false
        meets_criteria = True
        if numbers:  # if it is supposed to have number, set to true
            meets_criteria = has_number  # set meets_criteria to the has_number boolean value
        if special_character:
            meets_criteria = meets_criteria and has_special  # set meets_criteria to the last and has_special boolean value

    return pwd  # return the pwd variable with the characters


min_length = int(input("What is the minimum length? "))  # asks for the input for min_length
has_number = input(
    "Do you want numbers? (y/n) ").lower() == "y"  # ask if they want numbers, turns the answer to lower case and a boolean value if it == "y"
has_special = input(
    "Do you want special characters? (y/n) ").lower() == "y"  # ask if they want special chars, turns the answer to lower case and a boolean value if it == "y"
pwd = generate_password(min_length, has_number,
                        has_special)  # calls the function with the passing variables and assigns it to pwd
print(f"The generated password: {pwd}")  # prints the generated password
