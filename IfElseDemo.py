lang=input("Enter the programming language: ")  #

# lang="python"

if lang=="selenium":
    print("selenium found")
elif lang=="java":
    print("java found")
elif lang=="python":
    print("python found")
else:
    print("language not found")

print("************************")

print("welcome")
if 15>10:print("Yes")
print("bye")

marks=95
print("A+") if marks>90 else print("A")

print("************************")

sal=input("Enter your salary: ")
print(type(sal))
sal=int(sal)
# sal = 50000
if sal>40000:
    print("Eligible for a car loan")
    if sal>80000:
        print("Eligible for home loan")
        if sal>100000:
            print("Eligible for all loan")
else:
    print("Not eligible for any loan")