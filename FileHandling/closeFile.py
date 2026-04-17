with open("/Users/rajib/PythonTutorial/FileHandling/Demo.txt") as f:
    print("The file status is : ", f.closed)
    data = f.read()  # read the file content
    print(data)

print("The file status after with block is : ", f.closed)

import os

with open(os.path.dirname(os.getcwd())+"/Pythontutorial/FileHandling/Demo.txt") as f:
    data = f.read()
    print(data)

print("File is closed automatically after with block:", f.closed)