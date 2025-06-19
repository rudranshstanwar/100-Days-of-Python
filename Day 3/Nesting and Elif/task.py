print("Welcome to the roller coaster")
height = int(input("What is your height in cms? \n"))
bill = 0
if height >= 120:
    age = int(input("What is your age? \n"))
    if age <= 12:
        bill = 5
        print("Your amount is $5")
    elif age <= 18:
        bill = 7
        print("Your amount is $7")
    else:
        bill = 15
        print("Your amount is $15")
    photo = input("Do you want a photo type Yes for yes and No for No\n")
    if photo == "Yes":
        bill += 5
        print(f"Your total bill is \n${bill}")
    else:
        print(f"Your toatal bill is \n${bill}")
else:
    print("Come back after you have grown taller")
