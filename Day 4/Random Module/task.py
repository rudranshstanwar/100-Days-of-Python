import random
# We can multiply the range by any number in either one randint or random
print(random.randint(5, 9)*10.3)
# In random range is [0,1)
print(random.random()*15)
# For the random problem to be solved we use uniform
# The range of uniform is [a, b]
print(random.uniform(2,5))
number = random.randint(0,1)
if number == "0":
    print("Heads".upper())
else:
    print("tails".upper())
# For ramdomizing use randint or random or uniform