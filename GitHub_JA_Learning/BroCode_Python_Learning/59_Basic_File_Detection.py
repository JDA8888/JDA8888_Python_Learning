# Pythong file Detection


import os

file_path ="BroCode_Python_Learning/test.txt"  # relative file path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else: print("That file location doesn't exist")

file_path ="C:/Users/User_/Desktop/Python Code/BroCode_Python_Learning/test.txt"  # absoulte file path <--- Copy from file explorer, in this sample where Users/YOUR USER NAME HERE/Desktop for this to work. 

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else: print("That file location doesn't exist")