#Q1
#Please write a program which asks the user for an integer number. 
# The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

# Write your solution here
n1 = int(input("Please type in a number: "))

if n1 == 1984:
    print("Orwell")

#Q2 Please write a program which asks the user for an integer number. 
# If the number is less than zero, the program should print out the number multiplied by -1. 
# Otherwise the program prints out the number as is. 
# Please have a look at the examples of expected behaviour below.

n1 = int(input("Please type in a number: "))
n2 = n1 * -1

if n1 < 0:
    print(f"The absolute value of this number is {n2}")
else:
    print(f"The absolute value of this number is {n1}")
    
#Q3 Please write a program which asks for the user's name. If the name is anything but "Jerry",
# the program then asks for the number of portions and prints out the total cost.
# The price of a single portion is 5.90.


name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup? "))
    total_cost = portions * 5.90
    print(f"The total cost is {total_cost}")
    print("Next please!")
    
#Q4Please write a program which asks the user for an integer number. 
# The program should then print out the magnitude of the number according to the following examples.

n1 = int(input("Please type in a number: "))

if n1 < 1000:
    print("This number is smaller than 1000")
    
if n1 < 100:
    print("This number is smaller than 100")
if n1 < 10:
    print("This number is smaller than 10")
    
print("Thank you!")


#Q5 Please write a program which asks the user for two numbers and an operation. 
# If the operation is add, multiply or subtract, the program should calculate and print out the 
# result of the operation with the given numbers. 
# If the user types in anything else, the program should print out nothing.

n1 = int(input("Please type in a number: "))
n2 = int(input("Please type in  number: "))
op = input("Please type in an operation: ")

if op == "add":
    plus = n1 + n2 
    print(f"{n1} + {n2} = {plus}")
if op == "subtract":
    minus = n1 - n2
    print(f"{n1} - {n2} = {minus}")
if op == "multiply":
    multi = n1 * n2
    print(f"{n1} * {n2} = {multi}")
    
#Q6 Please write a program which asks the user for a temperature in degrees Fahrenheit,
# and then prints out the same in degrees Celsius. If the converted temperature falls
# below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")
    
    
#Q7 Please write a program which asks for the hourly wage, hours worked, 
# and the day of the week. The program should then print out the daily wages, 
# which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
H_wage = float(input("Please type in your wage: "))
H_worked = float(input("Please type in your hours worked: "))
day_week = input("Please type in the day: ")

if day_week != "Sunday":
    daily_wages = H_wage * H_worked
    print(f"Daily wages: {daily_wages}")
if day_week == "Sunday":
    daily_wages = (H_wage * H_worked)*2
    print(f"Daily wages: {daily_wages}")
    
    
#Q8 This program calculates the end of year bonus a customer receives on their loyalty card. 
# The bonus is calculated with the following formula:
#If there are less than a hundred points on the card, the bonus is 10 %
#In any other case the bonus is 15 % 
# Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.

points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

else:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

#q9 Please write a program for solving a quadratic equation of the form ax²+bx+c. 
# The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. 
# The quadratic formula expressed with the Python sqrt function is as follows:
#x = (-b ± sqrt(b²-4ac))/(2a).
#You can assume the equation will always have two real roots, so the above formula will always work.
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

quad_eq1 =(-b + sqrt(b**2 - 4*a*c))/(2*a)
quad_eq2 =(-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f"The Roots are {quad_eq1} and {quad_eq2}")


# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5