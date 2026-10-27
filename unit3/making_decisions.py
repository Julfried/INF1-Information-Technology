# temperature = float(input("Current temperature: "))
# cond = temperature > 30.0

# if cond:
#     print("Hot")
# else:
#     print("Cold")


# Multiple if statements
temperature_celsius = 35
if temperature_celsius > 30:
    print("Hot")
if temperature_celsius > 0:
    print("Above freezing")
if temperature_celsius < 0:
    print("Below freezing")

# elif vs if
temperature_celsius = 35
if temperature_celsius > 30:
    print("Hot")
elif temperature_celsius > 0:
    print("Above freezing")
elif temperature_celsius < 0:
    print("Below freezing")

# Else block
temperature_celsius =-5
if temperature_celsius > 30:
    print("Hot")
elif temperature_celsius > 0:
    print("Above freezing")
else:
    print("At or below freezing")
