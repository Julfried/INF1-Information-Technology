secret_word = "ipi lipikepe yopoupu"
result = ""
i = 0

while i < len(secret_word):
    result += secret_word[i]
    if secret_word[i] in "aeiou":
        i += 3
    else:
        i += 1
    print(result)

print("The final decoded string is: ")
print(result)