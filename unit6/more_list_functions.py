our_list = [1, 2,3, 4, 5]

# Common error with append
# Wrong
our_list_wrong = our_list.append(6)

# Correct 
our_list.append(6)

print(type(our_list_wrong))
print(type(our_list))
print(our_list_wrong)
print(our_list)

# More list methods
# Insert: Inserts a value at index
values = [10, 20, 30]
values.insert(1, 99)
print(values) 

# pop returns a value ==> can be assigned to a variable
removed = values.pop()
print(values)