# Nested list example
grid = [
    [1, 13, 2],
    [2, 12, 10],
    [39, 6, 13]
]

# Access the first row
val1 = grid[0]
print(val1)

val2 = grid[0][1]
print(val2)

# Get the first collum of this list
val3 = []
for elements in grid:
    val3.append(elements[0])
print(val3) # [1, 2, 39]