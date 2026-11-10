letters = "ABC"

# normal iteration
for letter in letters:
    print(letter)

# Iterating by index
for i in range(len(letters)):
    print(i, letters[i])

# Looping over multiple indices
lower_letters = "abc"
upper_letters = "ABC"
for i in range(len(lower_letters)):
    print(lower_letters[i], upper_letters[i])

