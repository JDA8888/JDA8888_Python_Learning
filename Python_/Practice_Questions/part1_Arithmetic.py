#Q1 Please write a program which asks the user for a number. 
#The program then prints out the number multiplied by five.
n1 = int(input("Please type in a number: "))
n2 = 5

n3 = n1 * n2
print (f"{n1} times {n2} is {n3}" )

#Q2 Please write a program which asks the user for a number of days.
days = int(input("How many days? "))
days1 = days * 24 * 60 * 60

print (f"Seconds in that many days: {days1}")

#Q3 
# Fix the code
number = int(input("Please type in the first number: "))
number1 = int(input("Please type in the second number: "))
number2 = int(input("Please type in the third number: "))

product = number * number1 * number2

print("The product is", product)

#Q4

n1 = int(input("Please type a number: "))
n2 = int(input("Please type a number: "))

number3 = n1 + n2
number4 = n1 * n2

print (f"The sum of the numbers: {number3}")
print (f"The product of the numbers: {number4}")

#Q5
n1 = int(input("Please type a number: "))
n2 = int(input("Please type a number: "))
n3 = int(input("Please type a number: "))
n4 = int(input("Please type a number: "))

s1 = n1 + n2 + n3 + n4
m1 = (n1 + n2 + n3 + n4)/4

print (f"The sum of the numbers is {s1} and the mean is {m1}")

#Q6
n1 = int(input("How many times a week do you eat at the student cafeteria? "))
n2 = float(input("The price of a typical student lunch? "))
n3 = float(input("How much money do you spend on groceries in a week? "))

daily = ((n1*n2) + n3)/7
weekly = (n1 * n2) + n3

print(f"Average food expenditure \n Daily: {daily} euros \n Weekly: {weekly} euros")

#Q7
students = int(input("How many students in the course? "))
group_size = int(input("Desired group size? "))

groups = (students + group_size - 1) // group_size

print(f"Number of groups formed: {groups}")