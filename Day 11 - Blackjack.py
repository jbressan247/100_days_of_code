from random import randint

playing = False
player_hand = []
dealer_hand = []
play = input("Do you want to play Blackjack? type 'y' or 'n' ").lower()

if play == "y":
    playing = True
else:
    playing = False

def win_checker(player_total, dealer_total):
    if player_total > dealer_total:
        print("Player Wins!")
    else:
        print("Dealer Wins!")


while playing:
    for hand in range(2):
        card_values = randint(1, 14)
        player_hand.append(card_values)
    for hand in range(2):
        card_values = randint(1, 13)
        dealer_hand.append(card_values)

    print(f"Dealer's first card: {dealer_hand[0]}")
    print(f"Player Hand: {player_hand}")

    player_total = 0
    for i in range(0, len(player_hand)):
        player_total = player_total + player_hand[i]

    dealer_total = 0
    for i in range(0, len(dealer_hand)):
        dealer_total = dealer_total + dealer_hand[i]


    if player_total < 21:
        is_hit = input("do you want to hit? type 'y' or 'n' ").lower()
        if is_hit == 'y':
            card_values = randint(1, 11)
            player_hand.append(card_values)
            player_total += card_values
            print(player_hand)
        else:
            print(f"Player hand: {player_hand}")
            print(f"Dealer Hand: {dealer_hand}")

    win_checker(player_total, dealer_total)
    play = input("Do you want to play Blackjack again? type 'y' or 'n' ").lower()
    if play == "y":
        playing = True
    else:
        playing = False
