temp = float(input("Enter a temperature in °C: "))

if temp < 0:
    print("Below freezing")
elif 0 <= temp <= 30:
    print("Normal range")
else:
    print("Hot")