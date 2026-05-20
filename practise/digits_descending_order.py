def descending_order(num):
    if num == 0:
        return 0

    arr = []

    while num > 0:
        digit = num % 10
        num = num // 10
        arr.append(digit)

    arr.sort(reverse=True)

    return int("".join(str(d) for d in arr))

print(descending_order(0))
print(descending_order(123456789))