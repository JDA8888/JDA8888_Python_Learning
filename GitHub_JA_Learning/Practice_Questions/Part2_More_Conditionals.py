#Q1 FIX THE SYNTAX 
#   number = input("Please type in a number: ")
#   if number>100
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred)
#      print("Its value is now"+ number)
#  print(number + " must be my lucky number!")
#  print("Have a nice day!)

number = int(input("Please type in a number: "))
if number>100:
    print("The number was greater than one hundred")
    number = number - 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number}")
print(f"{number} must be my lucky number!")
print("Have a nice day!")

#More Conditionals, // if, elif and else // also % modulo operation // section covers creating multiple branches. 
#Q1 Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.
n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in another number: "))

if n1 > n2:
    print("The greater number was:", {n1})
elif n1 < n2:
    print("The greater number was:", {n2})
elif n1 == n2:
    print("The numbers are equal!")
    
#Q2 Please write a program which asks for the names and ages of two persons.
#The program should then print out the name of the elder.
name1 = input("Person 1: ")
age1 = int(input("Age: "))
name2 = input("Person 2: ")
age2 = int(input("Age2: "))

if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")

#Q3Please write a program which asks the user for two words.
# The program should then print out whichever of the two comes alphabetically last.
n1 = input("Please type in a word: ")
n2 = input("Please type in a word: ")

if n1 > n2:
    print(f"{n1} comes alphabetically last.")
elif n2 > n1:
    print(f"{n2} comes alphabetically last.")
else:
    print("You gave the same word twice.")
    
#PART 4 COMBINING OPERATORS // and or not // 
#Q1 Please write a program which asks for the user's age. 
# If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, 
# the program should print out a comment.

age = int(input("What is your age? "))

if age < 0:
    print("That must be a mistake")
elif age >= 0 and age <= 4: 
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")

#Q2 Please write a program which asks for the user's name. If the name is Huey, Dewey or Louie, the program should recognise 
# the user as one of Donald Duck's nephews.
#In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

name = input("Please type in your name")

if name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
else:
    print("You are not a nephew of any character I know of.")
    
#Q3 The table below outlines the grade boundaries on a certain university course. 
# Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

grade = int(input("How many points [0-100]:"))

if grade < 0:
    print("Grade: impossible!")
elif grade >= 0 and grade <= 49:
    print("Grade: fail")
elif grade >= 50 and grade <= 59:
    print("Grade: 1")
elif grade >= 60 and grade <= 69:
    print("Grade: 2")
elif grade >= 70 and grade <= 79:
    print("Grade: 3")
elif grade >= 80 and grade <= 89: 
    print("Grade: 4")
elif grade >= 90 and grade <= 100:
    print("Grade: 5")
elif grade > 100:
    print("Grade: impossible!")

#Q4Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz.
# If the number is divisible by five, 
# the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.
n1 = int(input("Number: "))

if n1 % 3 == 0 and n1 % 5 == 0:
    print("FizzBuzz")
elif n1 % 3 == 0:
    print("Fizz")
elif n1 % 5 == 0:
    print("Buzz")
else:
    print(f"{n1}")

#Q5 NESTED CONITIONALS
#Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100,
# it is a leap year only if it also divisible by 400.
#Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("This is a leap year.")
elif year % 100 == 0:
    print("This is not a leap year.")
elif year % 4 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
    
#Q6 Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
#You may assume the letters will be either all uppercase, or all lowercase.
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if a > b:
    if a < c:
        middle = a
    elif b>c:
        middle = b
    else:
        middle = c
else:
    if b < c:
        middle = b
    elif a > c:
        middle = a
    else:
        middle = c
print("The letter in the middle is:", middle)

#Q7 Finnish Tax Calc Example
# Question Please write a program which calculates the correct amount of tax for a gift from a close relative. 
# Have a look at the examples below to see what is expected. Notice the lack of thousands separators in the input values - 
# you may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet covered dealing with these.
gift = int(input("Value of the gift: "))

t1 = (100 + (gift - 5000) * 0.08)
t2 = (1700 + (gift - 25000) * 0.10)
t3 = (4700 + (gift - 55000) * 0.12)
t4 = (22100 + (gift - 200000) * 0.15)
t5 = (142100 + (gift - 1000000) * 0.17)

if gift >= 5000 and gift < 25000:
    print(f"Amount of tax:", t1)
elif gift >= 25000 and gift < 55000:
    print(f"Amount of tax:", t2)
elif gift >= 55000 and gift < 200000:
    print(f"Amount of tax:", t3)
elif gift >= 200000 and gift < 1000000:
    print(f"Amount of tax:", t4)
elif gift >= 100000:
    print(f"Amount of tax:", t5)
else:
    print("No Tax!")


## PART 4 SIMPLE LOOPS 
#Q1 Let's create a program along the lines of the example above. This program should print out the message "hi" 
# and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. 
# Please have a look at the example below.


while True:
    print("hi")
    code = input("Shall we continue? ")

    if code == "no":
        break
print("okay then")

#Q2Please write a program which asks the user for integer numbers.
#If the number is below zero, the program should print out the message "Invalid number".
#If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
#In either case, the program should then ask for another number.
#If the user inputs the number zero, the program should stop asking for numbers and exit the loop.
from math import sqrt
# Write your solution here

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    elif number > 0:
        n1 = sqrt(number)
        print(n1)
    elif number == 0:
        break
print("Exiting...")

#Q3 Please write a program which asks the user for a password. The program should then ask the user to type in the password again. 
# if the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.
password = input("Password:")

while True:
    password2 = input("Repeat password: ")
    if password != password2:
        print("They do not match!")
    else:
        password == password2
        break
print("User account created!")

#Q4 Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
# The program should then print out the number of times the user tried different codes.
attempts = 0
c_pin = "4321"

while True:
    pin = input("Pin: ")
    attempts += 1
    if pin == c_pin:
        if attempts == 1:
            print("Correct It only took you one single attempt!")
        else:
            print(f"Correct! it yook you {attempts} attempts")
        break
    else:
        print("wrong")
        
#Q5 Part 1
#Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.
# Part 2 
#Change the program so that the loop ends also if the user types in the same word twice in a row.
story = ""
previous = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous:
        break
    story += word + " "
    previous = word

print(story)
    