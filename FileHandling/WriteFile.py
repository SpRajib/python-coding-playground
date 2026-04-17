with open("/Users/rajib/PythonTutorial/FileHandling/Demo.txt", "w") as f:

    f.write("\nThis is new line added in the file.") 
    # write mode will overwrite the file content 

with open("/Users/rajib/PythonTutorial/FileHandling/DemoRajib.txt", "w") as f:

    f.write("\nThis is new file created and new line added in the file.") 
    # write mode will create a new file if it does not exist
    
