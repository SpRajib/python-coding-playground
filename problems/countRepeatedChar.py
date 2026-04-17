#count frequency or repeated character in a string
str = "ABCABC"
char_count = {}

for ch in str:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print(char_count)