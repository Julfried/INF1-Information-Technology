# A list is a sequence of values
numbers = [20, 50, 4, 19, 15, 1]
words = ["one", "two", "hello"]
mixed = ["hello", 50, 365.25]

# The length of a list
print(len(mixed))

# Accessing individual elements in a list
text = mixed[0]
print(text)
print(len(mixed[0]))

# Indexing in lists
numbers = mixed[1:]
print(numbers)

# list of strings
words = ["one", "two", "hello"]
dictionary = [words, ["another word"]]
print(words[2])
print(words[2][1])
print(dictionary[0][2][1])

# Membership
words = ["one", "two", "hello"]

print("one" in words)
print("n" in words)

# Loop over a list
# Using a For loop
positions = [20, 50, 4, 19]
for value in positions:
    print(value)

# Using a While loop
i = 0
while i < len(positions):
    print(positions[i])
    i += 1
