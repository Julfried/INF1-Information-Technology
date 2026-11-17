input_sum = 0
i = 0

while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break
    else:
        i += 1
        input_sum += user_input

print(f"We did {i} iterations")
print(f"Sum is {input_sum}")
print(f"Mean is {input_sum / i}")
