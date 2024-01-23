from random import randint, choice
from blackjack_logo import logo


def deal_card():
	'''randomly selects a card from the card_values and deals it to the players'''
	card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = choice(card_values)
	return card


def calculate_score(hand):
	'''Take a list of cards and return the total score'''
	if len(hand) == 2 and sum(hand) == 21:
		return 0
	if 11 in hand and sum(hand) > 21:
		hand.remove(11)
		hand.append(1)
	return sum(hand)


def compare(player_total, dealer_total):
	'''Compare player total and dealer total'''
	if player_total > 21 and dealer_total > 21:
		return "You lose"
	elif player_total == dealer_total:
		return "it's a draw"
	elif player_total == 0:
		return "Blackjack! You win!"
	elif dealer_total == 0:
		return "Blackjack for the Dealer. You lose!"
	elif player_total > 21:
		return "You lose!"
	elif dealer_total > 21:
		return "Dealer loses!"
	elif player_total > dealer_total:
		return "Player wins"
	else:
		return "Dealer Wins!"


def play_blackjack():
	print(logo)

	player_hand = []
	dealer_hand = []
	game_over = False

	for hand in range(2):
		player_hand.append(deal_card())
		dealer_hand.append(deal_card())

	while not game_over:
		player_total = calculate_score(player_hand)
		dealer_total = calculate_score(dealer_hand)
		print(f"Here is the dealer's first card: {dealer_hand[0]}")
		print(f"Here is the player's hand: {player_hand}")
		if player_total == 0 or dealer_total == 0 or player_total > 21:
			game_over = True
		else:
			is_hit = input("Do you want to hit? type 'y' or 'n' ").lower()
			if is_hit == "y":
				player_hand.append(deal_card())
			else:
				game_over = True

	while dealer_total != 0 and dealer_total < 17:
		dealer_hand.append(deal_card())
		dealer_total = calculate_score(dealer_hand)

	print(f"Dealer's hand: {dealer_hand} | Dealer's Score {dealer_total}")
	print(f"Player's hand: {player_hand} | Player's Score {player_total}")
	print(compare(player_total, dealer_total))


while input("Do you want to play Blackjack? type 'y' or 'n' ").lower() == "y":
	play_blackjack()