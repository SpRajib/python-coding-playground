try:
    content = open("/Users/rajib/PythonTutorial/Exception_Handling/Demo1.txt", "r")
    print(content.read())

except FileNotFoundError as err:
    print("File not found error", err)

print("Execution continues...")