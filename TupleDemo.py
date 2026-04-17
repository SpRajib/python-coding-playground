tup1 = (1,"python",90.0,True,1,1,"Rajib",2,2,2)
print(tup1)

print(tup1[1]) # access tuple element using index
print(tup1[-1]) # access tuple element using negative index
print(tup1.count(1)) # count the occurrences of an element in the tuple
print(tup1.count(2)) # count the occurrences of an element in the tuple
print(tup1.index("Rajib")) # get the index of an element in the tuple
print(tup1[0:4]) # slicing the tuple
print(tup1[3:]) # slicing the tuple from index 3 to end
print(tup1[:5]) # slicing the tuple from start to index 5
print(tup1[::-1]) # reverse the tuple using slicing

print("**********************************************")

# tup1[0]="Mukesh" # trying to update the tuple element (this will raise an error as tuples are immutable)
