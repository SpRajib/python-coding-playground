#Reverse a string without using slicing.

str = "abc"

rev = ""
for ch in str:
    rev = ch+rev
print(rev)
