def find_average(numbers):
    # your code here
    total = 0
    count = 0
    if numbers == []:
        return 0
    else:
        for ele in numbers:
            count += 1
            total += ele
    
    return total/count

print(find_average([1, 2, 3, 4, 5]))
print(find_average([10, 20, 30]))