text = "abc.def"
print(text)

# Seprate the string into subtrings
substrings = text.split(sep=".")
print(substrings)

# Join back together
joined = ",".join(substrings)
print(joined)
