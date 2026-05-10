def stringPalindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
str = "level"
print(stringPalindrome(str))