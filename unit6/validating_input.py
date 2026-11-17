# Iterate until the user enters a correct input
while True:
    value = int(input("Enter a positive number: "))
    if value > 0:
        break
    print("Not positive. Try again.")
    print(f"You entered {value}")