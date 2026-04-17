name = ["Rajib", "Mukesh", "Akash"]
marks = [70,90,87]
address = ["abc","xyz","demo"]

data=zip(name,marks,address)  
print(data)

mydata = list(data) # returns in tuple inside list

a,b,c = zip(*mydata)
print(a)
print(b)
print(c)