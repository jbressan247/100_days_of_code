import secret_auction_logo

print(secret_auction_logo.logo)

print("Welcome to the Auction!")
more_bidders = True
bids = {}

while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more_bids = input("What there other bidders? (Yes or No) ").lower()
    if more_bids == "yes":
        print("--------------------\n"*10)
    else:
        for names in bids:
            current_bid = bids[names]
            max_bid = 0
            winner = ""
            if current_bid > max_bid:
                max_bid = current_bid
                winner = names
        print("********************\n")
        print(f"The winner is: {winner}! with a bid of: ${max_bid}\n")
        print("********************\n")
        more_bidders = False
