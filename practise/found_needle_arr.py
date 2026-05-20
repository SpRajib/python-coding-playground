def find_needle(haystack):
    # your code here
    for ele in haystack:
        if ele == "needle":
            result = haystack.index(ele)
    return f"found the needle at position {result}"
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))