from time import sleep

import Caesar_Cipher_Art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
			'q', 'r', 's', 't', 'u',
			'v', 'w', 'x', 'y', 'z']

print(Caesar_Cipher_Art.logo)

result = True


def caesar(start_text, shift_amount, cipher_direction):
	end_text = ""
	if shift_amount > 26:
		shift_amount = shift_amount % 26
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabet and char != " ":
			position = alphabet.index(char)
			new_position = position + shift_amount
			end_text += alphabet[new_position]
		else:
			end_text += char
	print(f"Processing...")
	sleep(5)
	print(f"Processing.....")
	sleep(2)
	print(f"The {cipher_direction}d message is {end_text}")


while result:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
	go_again = input("Do you want to run it again? (Yes or No) ").lower()
	if go_again == "yes":
		result = True
	elif go_again == "no":
		result = False
		print("Exiting the program...")
		sleep(5)
		exit()
