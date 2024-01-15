from random import choice

stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
	  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
  |   |
	  |
	  |
=========
''', '''
  +---+
  |   |
  O   |
	  |
	  |
	  |
=========
''', '''
  +---+
  |   |
	  |
	  |
	  |
	  |
=========
''']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list = ["cat", "dog", "bat"]
chosen_word = choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f"the word is : {chosen_word}")

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.

display = []
guessed = []

for i in chosen_word:
	display += "_"

print(f"The word is: {display}")
print(stages[lives])
print("\nLet's play Hangman!")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Use a while loop to let the user guess again.

end_of_game = False

while not end_of_game:
	guess = input("Guess a letter: ").lower()

	# Loop through each position in the chosen_word
	# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
	# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
	if guess in guessed:
		print("You've already guessed that letter")

	for position in range(word_length):
		letter = chosen_word[position]

		if letter == guess:
			display[position] = letter

	if guess not in display and guess not in guessed:
		lives -= 1
		print(f"The letter {guess} is not in the word!")
		print(stages[lives])
	if guess not in guessed:
		guessed += guess

	# Print 'display' and you should see the guessed letter in
	# the correct position and every other letter replace with "_".
	print(f"The word is: {display}")
	print(f"Letters guessed: {guessed}")

	if lives == 0:
		end_of_game = True
		print("You lose!")

	if "_" not in display:
		end_of_game = True
		print("You win!")
