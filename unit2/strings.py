# Some string variables
greeting = 'Hello, world'
digits = "1234"
message = "We're #1!"
quotation = 'I said, "Put it over"'
print(greeting)

# Immutability does not mean you cannot assign a new value to the variable
print(quotation)
quotation = "A new value"
print(quotation)

# Type conversions
x = 42
y = "42.1"
y = float(y)
print(y)

z = x + y
print(z)
print(type(z))

# Bool type conversions
print(bool(0)) # False
print(bool(1)) # True
print(bool(-5)) # True

print(bool("")) # False
print(bool("text")) # True
print(bool("False")) # True

print("Test")
print(bool("False"))