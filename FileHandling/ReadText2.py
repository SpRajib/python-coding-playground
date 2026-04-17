try:
    f = open("/Users/rajib/PythonTutorial/FileHandling/Demo.txt")

    data=f.read() # read the file content
    print(data)
    print(f.name) # file name
    print(f.mode) # file mode


except Exception as err:
    print("Error in file handling", err)

finally:
    f.close() # close the file
    print(f.closed) # check if file is closed or not