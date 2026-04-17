def CountWords(sents):
    word = sents.split()
    count = len(word)
    return count

sents = "This is Rajib From Bhubaneswar"
print(CountWords(sents))