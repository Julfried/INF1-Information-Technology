s = "zephyr"
i = 0
while i < len(s):
    if s[i] not in "aeiou":
        i += 1
        continue
    print(s[i], i)
    i += 1