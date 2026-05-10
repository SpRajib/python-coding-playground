str = "Hello world"
def frequencyOfChar(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(frequencyOfChar(str))