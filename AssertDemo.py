#syntax 
# assert <condition>, <error message>
assert True
print("Assertion passed")
# assert False, "Assertion failed"

assert "selenium" in "selenium with python", "Substring not found"
print("Substring found, assertion passed")

str1 = "python"
str2 = "python"
assert str1 == str2, f"{str1} and {str2} are not equal"
print("Strings are equal, assertion passed")

assert "selenium" in ["python", "java", "Zelenium"], "Element not fount"
print("Element found in the list, assertion passed")