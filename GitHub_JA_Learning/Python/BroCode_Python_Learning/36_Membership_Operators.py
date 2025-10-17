# Membership operators = used to whether a value or variable is found in sequence
# include but not limited to (string, list, tuple, set, or dictionary)
# 1. in
# 2. not in

word = "APPLE"

letter = input("Please guess a letter in the secret word: ")

if letter in word: #In is a boolean which returns true if the letter is found 
    print(f"There is a {letter} in the secret word.") # to use not in we would need to reverse the statments in the two print lines below. 
else:
    print(f"Our {letter} was not found.")
    

# Example --- SET --- 

students = {"John", "Alex", "Matt", "Brad"}

student = input("Please type in a student name: ")

if student not in students:
    print(f"{student} was not found in the system. ")
else:
    print(f"The {student} is in the system.")
    
# Example -- Dictonary -- 

grades = {"Sandy": "A",
          "Josh": "B",
          "Matt": "C", 
          "Alex": "D"}
student = input("Enter a name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found.")
    
# Example -- String -- 

email = "john@gmail.com"

if "@" in email and "." in email:
    print("Valid Email.")
else:
    print("Invalid Email.")

    