'''

l = [5, 2, 9, 1, 7]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)
'''
#--------OR------Bubble sort----------#

numbers = [5, 2, 9, 1, 7]

for i in range(len(numbers)):
    for j in range(0, len(numbers)-1-i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)