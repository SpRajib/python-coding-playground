def Anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not Anagram")

Anagram("silent","listen")