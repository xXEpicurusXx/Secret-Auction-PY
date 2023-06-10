import os

auction = {}
secret_auction = False

def clear ():
    # os.system("clr") #this is for apple OS
    clear = lambda: os.system('cls') #This is for windows
    clear()

print("Welcome! Lets play Secret Auction!")

def play(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not secret_auction:
    players_name = input("What is the players name? : ")
    players_bid = int(input("What is the players bid : $"))
    auction[players_name] = players_bid
    additional_players = input("Are there any additional playsers? (y/n) : ")
    if additional_players.lower() == "n":
        secret_auction = True
        play(auction)
    elif additional_players.lower() == "y":
        clear()
