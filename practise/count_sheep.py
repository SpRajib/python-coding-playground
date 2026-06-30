def count_sheep(n):
    # your code
    result = ""
    for i in range(1,n+1):
        result += f"{i} sheep..."
    
    return result

print(count_sheep(3))
print(count_sheep(5))