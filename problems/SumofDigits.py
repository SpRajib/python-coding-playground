def sumOfDigit(num):
    count = 0
    while (num>0):
        digit = num%10
        count = count+digit
        num = num//10
    return count

print(sumOfDigit(123))
print(sumOfDigit(723))
