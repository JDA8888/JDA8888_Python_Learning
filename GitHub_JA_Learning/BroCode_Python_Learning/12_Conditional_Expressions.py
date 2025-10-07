# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
    # Print or assign one of two values based on a condition, X if condition else Y
    
    
num = 5
print("Positive" if num > 0 else "Negative")

num1 = 6
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

num3 = 5 
a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

age = 19
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 30
weather = "HOT" if temperature >= 20 else "COLD"
print(weather)
user_role = "Admin"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)