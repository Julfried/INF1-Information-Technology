# Sets are unordered collections of unique elements
# example names
names = {"Anna", "Peter", "Anna"}
names.add("Lisa")
names.add("Peter") # Add Peter a second time

# Sets have a length similar to lists and tuples
print(len(names)) # 3 unique items in this set

# Check for membership
print("Anna" in names) # True

# Creating an empty set
empty = set()
print(len(empty)) # 0

# Set operations
office = {"Anna", "Peter"}
lab = {"Peter", "Lisa"}

print(office | lab) # Union
print(office & lab) # Intersection
print(office - lab) # Difference
print(lab - office) # Difference