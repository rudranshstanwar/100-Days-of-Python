print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
customers = int(input("How many people to split the bill? "))
total_per_person = float(((bill + bill*(tip/100))/customers))
print(f"Each person should pay: {round(total_per_person,2)}")

