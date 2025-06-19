import art
print(art.logo)
# TODO-1: Ask the user for input
bid = {}
x = True
while x:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bid[name] = price
    y = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n"*120)
    if y == "no":
        x = False
print(f"The winner is {max(bid, key = bid.get)} with a bid of ${bid[max(bid, key = bid.get)]}")


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


