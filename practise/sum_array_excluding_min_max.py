def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0

    arr.sort()

    total = 0
    for ele in arr[1:-1]:
        total += ele

    return total

print(sum_array([1, 2, 3, 4, 5]))  # Output: 9
print(sum_array([5, 1, 3, 2, 4]))