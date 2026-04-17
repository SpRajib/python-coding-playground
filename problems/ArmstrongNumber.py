def Armstrong(num):
    count = 0
    temp = num
    while num>0:
        digit = num%10
        digitCube = digit*digit*digit
        count = count+digitCube
        num = num//10
    
    if temp == count:
        print("Armstrong number")
    else:
        print("Not Armstrong Number")

Armstrong(153)