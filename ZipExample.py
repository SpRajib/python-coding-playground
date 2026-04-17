name = ["Rajib", "Mukesh", "Akash"]
marks = [70,90,87]
address = ["abc","xyz","demo"]

data=zip(name,marks,address)  
print(data)

mydata = list(data) # returns in tuple inside list
print(mydata)

l1 = [1,2,3,4] 
print(list(zip(l1)))

#using set
name = {"Rajib", "Mukesh", "Akash"}
marks = {70,90,87}

print(list(zip(name,marks)))