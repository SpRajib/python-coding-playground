def sort_array(arr):
    odds = sorted(x for x in arr if x%2 != 0)
    result = []
    odd_index=0
    
    for num in arr:
        if num % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(num)
    
    return result

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))