letters = "ABC"

# Iterate over index and value at the same time
for i, letter in enumerate(letters):
    print(i, letter)

# Looping over multiple indices
lower_letters = "abc"
upper_letters = "AB"
for l, u in zip(lower_letters, upper_letters):
    print(l, u)

text1 = "abcde"
text2 = "ABCDE"

for char1, char2 in zip(text1, text2):
    print(char1.capitalize() == char2)

# Reversed and sorted
for char in reversed("abc"):
    print(char) # c, b, a

for char in sorted("cab"):
    print(char) # a, b, c