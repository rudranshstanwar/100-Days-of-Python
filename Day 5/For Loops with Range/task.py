# the range of range is [a, b) which means the number at end is excluded
# and the syntax is range(a, b, c) where (c - 1) is the gap b\w the numbers
# using range() instead of loop
for s in range(1, 11, 1):
    print(s*10)
# range() has to be used with another function like loop, etc
sum = 0
for number in range(1, 101):
    sum += number
print(sum)