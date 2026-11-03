# Task 1
up_to = int(input("Up to which number to print: "))
for i in range(1, up_to + 1):
    print(f"2 x {i} = {2*i}")

# Task 2
up_to = int(input("Up to which number to print: "))
for i in range(1, up_to + 1):
    print(f"Table for {i}")
    for j in range(1, up_to + 1):
        print(f"{i} x {j} = {i*j}")
    print("\n")