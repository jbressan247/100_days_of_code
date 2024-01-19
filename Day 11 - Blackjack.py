from random import randint, choice

player_playing = False
player_hand = []
dealer_hand = []
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
	return choice(card_values)


for hand in range(2):
	player_hand.append(deal_card())
	dealer_hand.append(deal_card())


def calculate_score(hand):
	total_score = sum(hand)
	if len(hand) == 2 and total_score == 21:
		return 0
	elif 11 in hand and total_score > 21:
		hand.append(1)
		hand.remove(11)
		return total_score
	else:
		return total_score


dealer_total = calculate_score(dealer_hand)
print(dealer_total)


def compare(player_total, dealer_total):
	if player_total == dealer_total:
		print("it's a draw")
		quit()
	elif player_total == 0:
		print("Blackjack! You win!")
		quit()
	elif dealer_total == 0:
		print("Blackjack for the Dealer. You lose!")
		quit()
	elif player_total > 21:
		print("You lose!")
		quit()
	elif dealer_total > 21:
		print("Dealer loses!")
		quit()
	elif player_total > dealer_total:
		print("Player wins")
		quit()
	elif dealer_total > player_total:
		print("Dealer Wins!")
		quit()


is_playing = input("Do you want to play blackjack? type 'y' or 'n' ")
if is_playing == "y":
	player_playing = True
else:
	quit()

while player_playing:
	player_total = calculate_score(player_hand)
	print(player_total)
	if player_total < 21:
		is_hit = input("Do you want to hit? type 'y' or 'n' ").lower()
		if is_hit == "y":
			player_hand.append(deal_card())
			print(player_total)
			print(player_hand)
			calculate_score(player_hand)
			compare(player_total, dealer_total)
		else:
			player_playing = False
			print(player_total)
			print(player_hand)
			calculate_score(player_hand)
			compare(player_total, dealer_total)
	else:
		print(player_total)
		print(player_hand)
		calculate_score(player_hand)
		compare(player_total, dealer_total)
		player_playing = False

# def starting_hand():
# 	for hand in range(2):
# 		player_hand.append(choice(card_values))
# 		dealer_hand.append(choice(card_values))
# 	print(f"Player's Starting Hand: {player_hand}")
# 	print(f"Dealer's First Card: {dealer_hand[0]}")
# 	return player_hand, dealer_hand
#
#
# def hit():
# 	is_hit = input("do you want to hit? type 'y' or 'n' ").lower()
# 	if is_hit == 'y':
# 		player_hand.append(choice(card_values))
# 		print(f"Player's Hand: {player_hand}")
# 		hit()
# 	elif is_hit == 'n':
# 		win_checker(player_total, dealer_total)
#
#
# def is_ace():
# 	if 11 in player_hand or 1 in player_hand:
# 		ace = int(input("do you want the ace to be 11 or 1? "))
# 		print(ace)
# 		player_hand.remove(11)
# 		player_hand.append(ace)
# 		print(player_hand)
# 	else:
# 		return "No Ace in hand"
#
#
# def win_checker(player_total, dealer_total):
# 	if player_total > 21:
# 		print("You lose!")
# 		playing = False
# 		return False
# 	elif dealer_total > 21:
# 		print("Dealer Loses, Player Wins!")
# 		playing = False
# 		return False
# 	elif player_total <= 21:
# 		print("out of the loop")
#
#
# def is_playing():
# 	play = input("Do you want to play Blackjack? type 'y' or 'n' ").lower()
# 	if play == "y":
# 		playing = True
# 	else:
# 		return False
#
# while playing:
# 	starting_hand()
# 	dealer_total = 0
# 	player_total = 0
# 	for i in range(0, len(player_hand)):
# 		player_total = player_total + player_hand[i]
# 	for i in range(0, len(dealer_hand)):
# 		dealer_total = dealer_total + dealer_hand[i]
#
# 	win_checker(player_total, dealer_total)
#
# is_playing()
