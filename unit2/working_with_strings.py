# 2 ways of defining a long string
message = "Hello, " \
"world"
print(message)

message = """Hello,
world"""
print(message)

# String methods
x = "this is a string"
print(x)
x = x.capitalize()
y = x.upper()
print(x.upper())

# Quiz
print("aaaa".count("aa")) # 2

# Word counter
text = "this is a string with a few words"
print(text.count(" ")) # 7 spaces, but 8 words
number_of_words = text.count(" ") + 1
print(f"The sentence has {number_of_words} words") # 8