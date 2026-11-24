# list
values = [10, 20, 30]
print(values[0])
values[0] = 99

# tuple
values1 = (10, 20, 30)
print(values1[0])
print(len(values1))
# values1[0] = 11

# Unpacking
var1 = values1[0]
var2 = values1[1]
var3 = values1[2]

var1, var2, var3 = values1
print(var1, var2, var3)

# Also works the other way around
values2 = 1, 2, 3

