# While loop with else statement
num = 10
while num < 15:
    print("num is:", num)
    num += 1
else:
    print("Loop ended as num is no longer less than 15")


print("************************")

# While loop with break statement
num = 5
while num<15:
    print("num is:", num)
    num += 1
    if num == 10:
        print("Breaking the loop as num is 10")
        break
else:
    print("Loop ended as num is no longer less than 15")

print("************************")

# While loop with continue statement
num = 1
while num < 10:
    num += 1
    if num ==5:
        continue
        print("This will not be printed when num is 5")
    print("num is:", num)
else:
    print("Loop ended as num is no longer less than 10")

print("************************")

# while loop with pass statement
num = 1
while num < 5:
    if num == 3:
        pass  # Placeholder for future code
        print("Pass statement executed when num is 3")
    print("num is:", num)
    num += 1
else:
    print("Loop ended as num is no longer less than 5")

print("************************")

feedback=""
while feedback not in ["1","2","3","4","5"]:
    feedback=input("Please rate our service from 1 to 5: ")
    print("thank you for your feedback:", feedback)
else:
    print("You rated our service as:", feedback)