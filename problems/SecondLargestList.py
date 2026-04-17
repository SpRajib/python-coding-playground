l1 = [12,34,21,56]
l1.sort()
data = l1[-2]
print(data)

numbers = [10, 25, 47, 99, 56]

first = second = float('-inf')
for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest number:", second)