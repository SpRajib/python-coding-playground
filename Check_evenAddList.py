def check_even(list1):
    even_nums = []
    odd_nums = []
    for i in list1:
        if i%2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)

    # return even_nums
    return odd_nums

numbers = [10, 15, 22, 33, 42, 55, 60]
# even_numbers = check_even(numbers)
odd_numbers = check_even(numbers)
# print("Even numbers in the list:", even_numbers)
print("Odd numbers in the list:", odd_numbers)