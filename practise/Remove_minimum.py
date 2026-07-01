def remove_smallest(numbers):
    if not numbers:
        return []

    result = numbers.copy()
    result.remove(min(result))
    return result

print(remove_smallest([5, 3, 2, 1, 4]))  # Output: [5, 3, 2, 4]
print(remove_smallest([1, 2, 3, 4, 5]))  # Output: [2, 3, 4, 5]