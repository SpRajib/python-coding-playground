def secondLargest(lst):
    new_lst = sorted(lst)
    return new_lst[-2]

print(secondLargest([1, 2, 3, 4, 5]))