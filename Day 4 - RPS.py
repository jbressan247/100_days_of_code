import random
import sys

wins = 0
losses = 0
ties = 0
# keep track of win rate

while True:  # main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:  # the player input loop
        player_move = input("Enter your move: (R)ock, (P)aper, (S)cissors or (Q)uit")
        player_move = player_move.upper()
        if player_move == "Q":
            sys.exit()  # quit the program
        if player_move == "R" or player_move == "S" or player_move == "P":
            break  # break of player input loop
        print("Type: R, S, P, or Q")

# Display what the player chose:vx
    if player_move == "R":
        print("Rock x....")
    elif player_move == "S":
        print("Scissors x....")
    elif player_move == "P":
        print("Paper x....")

# Display what the computer chose:
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = "R"
        print("Rock!")
    elif random_number == 2:
        computer_move = "S"
        print("Scissor!")
    elif random_number == 3:
        computer_move = "P"
        print("Paper!")

# Display and record win/lose
    if player_move == computer_move:
        print(f"TIED! {wins} win(s) |{losses} loss(es) | {ties} tie(s) |")
        ties += 1
    elif player_move == "R" and computer_move == "S":
        print(f"You Win! {wins} win(s) |{losses} loss(es) | {ties} tie(s) |")
        wins += 1
    elif player_move == "P" and computer_move == "R":
        print(f"You Win! {wins} win(s) |{losses} loss(es) | {ties} tie(s) |")
        wins += 1
    elif player_move == "S" and computer_move == "P":
        print(f"You Win! {wins} win(s) |{losses} loss(es) | {ties} tie(s) |")
        wins += 1
    elif player_move == "R" and computer_move == "P":
        print(f"You Lose! {wins} win(s) | {losses} loss(es) | {ties} tie(s) |")
        losses += 1
    elif player_move == "S" and computer_move == "R":
        print(f"You Lose! {wins} win(s) | {losses} loss(es) | {ties} tie(s) |")
        losses += 1
    elif player_move == "P" and computer_move == "S":
        print(f"You Lose! {wins} win(s) | {losses} loss(es) | {ties} tie(s) |")
        losses += 1
