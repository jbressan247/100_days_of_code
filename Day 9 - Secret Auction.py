import secret_auction_logo

print(secret_auction_logo.logo)

print("Welcome to the Auction!")
bidding = True
bids = {}


def find_highest_bid(bids):
	max_bid = 0
	winner = ""
	for names in bids:
		current_bid = bids[names]
		if current_bid > max_bid:
			max_bid = current_bid
			winner = names
	print("********************\n")
	print(f"The winner is: {winner}! with a bid of: ${max_bid}\n")
	print("********************\n")


while bidding:
	name = input("What is your name?: ")
	bid = int(input("What is your bid?: $"))
	bids[name] = bid
	more_bids = input("is there other bidders? (Yes or No) ").lower()
	if more_bids == "yes":
		print("--------------------\n" * 10)
	else:
		find_highest_bid(bids)
		bidding = False
