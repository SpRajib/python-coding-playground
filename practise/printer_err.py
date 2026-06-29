def printer_error(s):
    count = 0
    error_count = 0
    for char in s:
        count += 1
        if char not in 'abcdefghijklmABCDEFGHIJKLM':
            error_count += 1
    return f"{error_count}/{count}"

print(printer_error("aaabbbbhaijjjm"))
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))
print(printer_error("aaabbbbhaijjjmxyz"))