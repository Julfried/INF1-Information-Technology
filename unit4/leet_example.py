# Leet code exercise solution
user_text = input("Input any text: ")

for char in user_text:
    if char in "Ll":
        print(1)
    elif char in "Ee":
        print(3)
    elif char in "Tt":
        print(7)
    elif char in "Oo":
        print(8)
    else:
        print(char)
