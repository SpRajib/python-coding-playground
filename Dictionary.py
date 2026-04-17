emp = {"QA":"Mukesh", "Dev":"John", "HR":"Sara", "security":80, 50:"Python"}
print(emp)
print(type(emp))
print(emp["Dev"]) # access value using key
print(emp.get("QA")) # access value using get() method

emp = {"QA":["Mukesh","Rahul","David"],"dev":"Akash"}
print(emp["QA"][1]) # access list element inside dictionary
emp1=emp["QA"]
print(emp1[2]) # access list element using another variable

emp = {"QA":"Mukesh","dev":{"frontend":"Akash","backend":"John"}}
print(emp.get("dev").get("backend")) # access nested dictionary value
print(emp["dev"]["frontend"]) # access nested dictionary value using another way

emp["manager"]="Rajib" # add new key-value pair
print(emp)

emp["manager"] = "Satya" # update existing key-value pair
print(emp)

emp.pop("QA") # remove key-value pair using pop() method
print(emp)

print("\n")

emp.popitem() # remove last inserted key-value pair using popitem() method
print(emp)

print("\n*********************************************")
emp = {"QA":"Mukesh","dev":{"frontend":"Akash","backend":"John"}}
emp["HR"] = "Rajib"

print(len(emp)) # print the length of the dictionary

print(emp.keys()) # print all keys of the dictionary
print(emp.values()) # print all values of the dictionary
print(emp.items()) # print all key-value pairs of the dictionary (Tuples)

del emp["QA"] # delete specific key-value pair
print("\n",emp)
del emp # delete the entire dictionary
# print(emp) # this will raise an error as the dictionary is deleted
