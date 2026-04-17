evenList=[]
oddList=[]

for x in range(30):
    if x%2==0:
        evenList.append(x)
    else:
        oddList.append(x)

print("Even Numbers:", evenList)
print("Odd Numbers:", oddList)