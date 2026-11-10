"""https://de.wikipedia.org/wiki/Palindrom"""

text = input("Enter a text to be checked: ")
text = text.replace(" ", "")
text = text.replace(",", "")
errors = 0

for char, r_char in zip(text, reversed(text)):
    if char.lower() != r_char.lower():
        errors = errors + 1

if errors > 0:
    print(f"The text is not a palindrome with {errors} errors")
else:
    print("The text is a palindrome")
