# a String is a series of characters

name = input("Enter your full name: ")

# Len checks the length of a string, this also includes spaces
result = len(name)
print(result)
# This finds the position of the string section required, for example spaces. 

result1 = name.find(" ")
print(result1)

result2 = name.rfind("o")
print(result2)

# Cap a Letter

result3 = name.capitalize()
print(result3)
# Makes all upper case
result4 = name.upper()
print(result4)
# Makes all lower case
result5 = name.lower()
print(result5)

result6 = name.isdigit()
print(result6)

result7 = name.isalpha()
print(result7)
# Counters the string you ask for eg below. 

phone_number = input("Please enter your phone number: ")
result8 = phone_number.count("-")
print(result8)

phone_number = input("Please enter your phone number: ")
result9 = phone_number.replace("-"," ")
print(result9)
## This function below shows all the functions you can do. 
print(help(str))