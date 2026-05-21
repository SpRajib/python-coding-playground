def dig_pow(n, p):
    # your code
    total = 0
    for digit in str(n):
        total += int(digit)**p
        p += 1
    
    if total % n == 0:
        return total//n
    else:
        return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))