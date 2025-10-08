# Python writing files (.txt, .json, .csv)
import json
import csv


txt_data = "I like Lollies"

## Example 1

file_path = "output.txt" # reletive # absolute file path will look like --- C:\Users\INPUT USER HERE\Desktop   <--- input user here refers to the name

with open(file=file_path, mode="w") as file: # w = write | x = write if file exists | a = append a file | r = read a file 
    file.write(txt_data)
    print(f"Text file {file_path} was created. ")
    
## Example 2
try:    
    with open(file=file_path, mode="x") as file: # w = write | x = write if file exists | a = append a file | r = read a file 
        file.write(txt_data)
        print(f"Text file {file_path} was created. ")
except FileExistsError:
    print("That file already exists!")
    
## Example 3

try:    
    with open(file=file_path, mode="a") as file: # w = write | x = write if file exists | a = append a file | r = read a file 
        file.write("\n" + txt_data) # This creates a new line in the text document we are creating / writing  -- output would produce 2 lines of "I like Lollies" each time we run this the lines will increase e.g. run 5 times have additional lines. 
        print(f"Text file {file_path} was created. ")
except FileExistsError:
    print("That file already exists!")
    

## Example 4 

employees = ["Alex", "John", "Josh", "Bob"]

try:    
    with open(file=file_path, mode="x") as file: 
        for employee in employees:
            file.write(employee + " ") # this also creates a space in between each list item of employees 
        print(f"Text file {file_path} was created. ")
except FileExistsError:
    print("That file already exists!")
    
## Example 5 -- ENSURE YOU import json --- for the follow code to work. 

employee = {
    "name":"Alex",
    "age": 33,
    "job": "Fast Car Driver"
}

file_path1 = "output1.txt"

try:    
    with open(file=file_path1, mode="x") as file: 
        json.dump(employee, file, indent= 4)
        print(f"Text file {file_path1} was created. ")
except FileExistsError:
    print("That file already exists!")
    
## Example 6 -- CSV files (comma seperated values) common with an excel spreadsheet type of data. ---- note: Ensure to import csv for following code to work ----

employees = [["Name", "Age", "Job"],
             ["Alex", 33, "RocketMan"],
             ["Sandy", 28, "Flying Person"],
             ["John", 30, "Super Spy"]]


file_path2 = "output2.txt"

try:    
    with open(file=file_path2, mode="w", newline="") as file: 
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"Text file {file_path2} was created. ")
except FileExistsError:
    print("That file already exists!")