# To add all the values use sum(iterable datatype)
# Iterable datatypes are the one which can be looped

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89,
                  86, 55, 91, 64, 89]
# To do sum manually
sum = 0
for score in student_scores:
    sum += score
print(sum)

# To find max of a list use max()
print(max(student_scores))

# To find max manually
f = 0
for score in student_scores:
    if score > f:
        f = score
        print(f)



print(range(1, 10))
