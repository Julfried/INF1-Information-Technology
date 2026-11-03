# Structure of a for loop
secret_word = "olive"

for char in secret_word:
    print("Letter: " + char)

# Multiple statements
print("\nMultiple statements in the for loop")
for char in secret_word:
    print("Letter: " + char)
    print("*")

# Combine with if statement
print("\nCombined with if statements")
title = "The Escape"

for char in title:
    if char.isupper():
        print(char)