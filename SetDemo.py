mySet = {90,89,76,12,2,888}
print(mySet) # print the set with no index , every time in different order

mySet = {90,89,76,12,2,888,90,12} # set with duplicate elements
print(mySet) # print the set with no duplicate elements

mySet.add(777) # add element to the set
print(mySet)

mySet.pop() # remove and return an arbitrary element from the set
print(mySet)

mySet.remove(76) # remove specific element from the set
print(mySet)

mySet.discard(1000) # discard specific element from the set (no error if not found)
print(mySet)

# What is the difference between pop, remove and discard?
print(len(mySet)) # print the length of the set

mySet1 = mySet.copy() # copy the set
mySet.clear() # clear the set
print(mySet)  # print the empty set
print(mySet1) # print the copied set

print("\n")
# mySet2 = {90,89,76,12,2,888,90,90,"Rajib",90.0}
mySet2 = set(["Rajib",29.12,1,2,3,4])
print(mySet2) # print the set created from a list

mySet3 = set(("Rajib",29.12,1,2,3,4)) # set created from a tuple
print(mySet3) # print the set created from a tuple