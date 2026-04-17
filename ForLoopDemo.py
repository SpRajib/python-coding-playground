name = "python"

# for i in name:
    # print(i)

marks = [95, 85, 75, 65, 55]
final_marks = 0
for m in marks:
    final_marks = final_marks + m
print("Final Marks:", final_marks)
print("bye")

set = {10, 20, 30, 40}
for s in set:
    print(s)

dict = {"name":"python", "version":3.9, "type":"programming"}
for d in dict:
    print(d)  # prints the keys

for d in dict.items():
    print(d)  # prints the key-value pairs
for d,b in dict.items():
    print(d)  # prints the key-value pairs
    print(b)
for d in dict.values():
    print(d)  # prints the key-value pairs

print("************************")

for i in range(0,51):
    print(i, end=" ")