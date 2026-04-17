
def Ispalindrome(str):
    rev = str[::-1]
    if str==rev:
        print("palindrome")
    else:
        print("Not palindrome")

str = input("Enter a string to check : ")
Ispalindrome(str)