# Python reading files (.txt, .json, .csv)


# Example 1 
file_path = "BroCode_Python_Learning\output.txt"

with open(file_path, "r") as file: # r = read 
    content = file.read()
    print(content)
    
# Example 2 -- lets say we cant find this file 

file_path = "BroCode_Python_Learning\output.txt"

try:
    with open(file_path, "r") as file: # r = read 
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found.")
    
# Example 3 -- Permission Error -- 

file_path = "BroCode_Python_Learning\output.txt"

try:
    with open(file_path, "r") as file: # r = read 
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found.")    
except PermissionError:
    print("You do not have Permission to read that file. Its Top Level Security for spy's only... ")