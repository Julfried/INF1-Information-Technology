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

# Second version
output = ""
for char in user_text:
    if char in "Ll":
        output = output + "1"
    elif char in "Ee":
        output = output + "3"
    elif char in "Tt":
        output = output + "7"
    elif char in "Oo":
        output = output + "0"
    else:
        output = output + char

    print("Progress: ", output)

print("Final: ", output)
