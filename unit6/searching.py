# Use while loop for searching
s = "zephyr"
i = 0

while i < len(s) and s[i] != "y":
    i += 1
    
print(i) # 4
print(s[i])

# Expert Python Knowledge: Short circuit evaluation
s = "zephyr"
i = 6
print(i < len(s) and s[i] != "y")
print(s[i] != "y" and i < len(s)) # IndexError