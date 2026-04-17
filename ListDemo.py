list1 = [10,20,30,60]
print(list1)
print(type(list1))
list2 = ["Rajib",10,12.90,True]
print(list2)
print(len(list2))

list3 = list1+list2
print(list3)

print(list3[4])
print(list3[-1]) # last element
print(list3[1:5]) # elements from index 1 to 4

list4 = [10,32,45,90,90,90] # list with duplicate elements
print(list4)
print(list4.count(90)) # count occurrences of 90
print(list4.index(45)) # index of first occurrence of 45
print(list4[::-1]) # reverse the list

list4[1]=666 # modify element at index 1
print(list4)

list4.append(777) # add element at the end
print(list4)

list4.append("Python") # add another element at the end
print(list4)

list4.insert(0,222) # insert element at index 0
print(list4)
list4.insert(2,444) # insert element at index 2
print(list4)

list1.extend(list2) # extend list1 by adding elements of list2
print(list1)

list5="RAJIB" # list is iterable of characters
list1.extend(list5) # extend list1 by adding each character of the string as separate elements
print(list1)

list1.pop() # remove last element
print(list1)
list1.pop(2) # remove element at index 2
print(list1)

list1.remove(10) # remove first occurrence of value 10
print(list1)
list1.remove("Rajib") # remove first occurrence of value "Rajib"
print(list1)

print("\n")

list6=[12,89,78,90,55,44,8,3,2]
print(list6)
list6.sort() # sort the list in ascending order
print(list6)

list6.reverse() # reverse the list
print(list6)

print("\n")

nestedList = [10,20,[30,40,50],60,[70,80]]
print(nestedList)
print(nestedList[2]) # access the nested list at index 2
print(nestedList[2][1]) # access element at index 1 of the nested list at index 2
print(nestedList[4][0]) # access element at index 0 of the nested list at index 4