# Lists are mutable: you can replace an item at an existing index.
chars = ["h", "e", "l", "l", "o"]
chars[0] = "j"
print(chars)

# Uncomment one example at a time to see its error.

# TypeError: Strings are immutable. You cannot change a character in place.
# text = "hello"
# text[0] = "j"

# IndexError: This list has indices 0 through 4. Assignment cannot extend it.
# chars[5] = "q"

# Use append to add an item at the end.
chars.append("q")
print(chars)

# Inserting at index 0 shifts all existing items to the right.
chars.insert(0, "q")
print(chars)
