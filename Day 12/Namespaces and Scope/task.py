enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# A variable within a function is only accessible within the function
# outside the function it is not valid which means it has local scope


