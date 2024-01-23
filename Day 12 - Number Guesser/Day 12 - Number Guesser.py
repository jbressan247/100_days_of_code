from random import randint
from time import sleep
from num_guess_art import logo

low_num = 1
high_num = 10


def play():
	print(logo)
	print("Welcome to the Number Guessing Game!")
	print(f"I'm thinking of a number between {low_num} and {high_num}\n")
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or type 'quit' to exit ").lower()
	if difficulty == "quit":
		exit()

	elif difficulty == "hard":
		attempts = 5

	elif difficulty == "easy":
		attempts = 10

	num = randint(low_num, high_num)
	print(f"The difficulty is : {difficulty}")
	while attempts != 0:
		print(f"You have {attempts} attempt[s] remaining.")
		guess = int(input("Make a guess: "))
		if guess > num:
			print("Too High")
			attempts -= 1
		elif guess < num:
			print("Too low")
			attempts -= 1
		elif guess == num:
			print(f"You Guessed it! The number is {num}")
			break
		if attempts == 0:
			print("You've run out of guesses, you lose. ")
	sleep(2)
	play()


play()
