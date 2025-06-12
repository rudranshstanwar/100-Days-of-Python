print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# To define what these terms mean.
price = 0
price_cheese = 1
price_pep = 0
bill = 0
# If the size is Small
if size == "S":
    price = 15
    # Chose pepperoni as the subject for next case.
    if pepperoni == "Y":
        price_pep = 2
        if extra_cheese == "Y":
            bill = price + price_pep + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price + price_pep
            print(f"Your final bill is: ${bill}.")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            bill = price + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price
            print(f"Your final bill is: ${bill}.")
# Did Similar for other cases.
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price_pep = 3
        if extra_cheese == "Y":
            bill = price + price_pep + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price + price_pep
            print(f"Your final bill is: ${bill}.")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            bill = price + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price
            print(f"Your final bill is: ${bill}.")
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price_pep = 3
        if extra_cheese == "Y":
            bill = price + price_pep + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price + price_pep
            print(f"Your final bill is: ${bill}.")
    elif pepperoni == "N":
        if extra_cheese == "Y":
            bill = price + price_cheese
            print(f"Your final bill is: ${bill}.")
        else:
            bill = price
            print(f"Your final bill is: ${bill}.")
# To show that the given input is invalid.
else:
    print("error404")




