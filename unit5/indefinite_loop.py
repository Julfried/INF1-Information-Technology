num = 0

# First example
while num < 5:
    print(num)
    num = num + 1

# Zero iteration while loop
num = 5
while num < 3: # False at the start
    print(num)

print("Finished") # only this line prints

# Concept Check:
x = 6
while x > 4:
    x = x- 1
    print(x)

# Nested while loop
i = 0
while i < 3:
    j = 8
    while j < 11:
        print(i, j)
        j += 1
    i += 1

# Combine with boolean operators
x = 4
y = 10
print("Boolean operators: ")
while x <= 10 and y <= 13:
    print(x, y)
    x += 1
    y += 1