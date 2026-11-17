# Stop the loop iterations immediately with break
s = "zephyr"
i = 0
while i < len(s):
    if s[i] == "y":
        break
    i += 1
print(i) # 4
print(s[i])

# VS stopping the loop based on condition
s = "zephyr"
i = 0

while i < len(s) and s[i] != "y":
    i += 1

print(i) # 4
print(s[i])