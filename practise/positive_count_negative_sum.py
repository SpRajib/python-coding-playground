def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count = 0
    sum = 0
    l = []
    for num in arr:
        if num > 0:
            count += 1
        elif num < 0:
            sum += num

    return [count , sum]

print(count_positives_sum_negatives([1, 2, 3, -1, -2, -3]))