status = False

names = ["python", "java", "c++", "ruby"]

for i in names:
    if i == "java":
        status = True
        break # come out of the loop
    else:
        print("Still we re searching....")
    
if status:
    print("java found")
else:
    print("java not found")

