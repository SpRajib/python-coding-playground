def ReverseWordsSentence(sents):
    word = sents.split()
    rev = " ".join(word[::-1])

    return rev

sents = "This is Rajib"
print(ReverseWordsSentence(sents))