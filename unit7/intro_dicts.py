# Store name + age in 2 variables
names = ["Julia", "Peter", "Max"]
ages = [23, 24, 25]

# Much easier
dictionary = {"Julia": 23, "Peter": 24, "Max": 25}

# How old is Max?
# list
max_age = 0
for name, age in zip(names, ages):
    if name == "Max":
        max_age = age

print(f"Max is {max_age} years old")

# dict
print(f"Max is {dictionary['Max']} years old")

# A missing key will raise a KeyError
ages = {
"Anna": 22,
"Peter": 25
}
# print(ages["Tom"]) # KeyError: 'Tom

print("Tom" in ages)
print("Anna" in ages)

# Use get to avoid the KeyError
tom_age = ages.get("Tom")
if tom_age != None:
    print(f"Tom is {tom_age} old")
else:
    print("Tom is not in dictionary")

# Looping over a dict
# Per default you will iterate over the keys in the dict
for key in dictionary:
    print(key)

# Iterate over the values
for value in dictionary.values():
    print(value)

# Iterate over keys and values
for k, v in dictionary.items():
    print(f"key: {k} -> value: {v}")