tup1 = (1,"python",90.0,True,1,1,"Rajib",2,2,2)
print(type(tup1))
print(tup1)

list = list(tup1) # convert tuple to list
print(type(list))
print(list)

set = set(tup1) # convert tuple to set
print(type(set))
print(set)

print("**********************************************")

tup2 = ("Mukesh") 
print(tup2)
print(len(tup2))  # 6 

tup2 = ("Mukesh",12) 
print(tup2)
print(len(tup2))  # 1

l1 = [(1,3,5),(2,4,6),(7,8,9)]
print(l1[0])
print(l1[1][2])

t1 = tuple(["Mukesh","Rajib","David"])
print(t1)
print(type(t1))