
# Operator Precedence
print(not True or True and False)
# True
# Same grouping:
print(True or (True and False))
# True
# Different grouping:
print((True or True) and False)
# False

# temperature example
temperature_celsius = 35
is_ready = False
if temperature_celsius > 30 or temperature_celsius < 0 and is_ready:
    print("Check sensor")
else:
    print("No check")