def find_short(s):
    words = s.split()
    
    shortest = len(words[0]) # Initialize shortest to the length of the first   word

    for word in words:
        if len(word) < shortest:
            shortest = len(word)

    return shortest

print(find_short("bitcoin take over the world maybe who knows perhaps"))