# Print Function
print ("Hello Joel")
# Second line of code 
print("Hello world its a great day today")

# Vairable = A container for a value (string, interger, float, boolean) A variable behaves as if it was the value it contains

first_name = "Joel"
food = "pizza"
email = "joel123@fake.com"
print(f"Hello {first_name}, you like eating {food}, this is your email, {email}")

# Integers
age = 33
quantity = 3
num_students = 164
print(f"you are {age} old, and you are buying {quantity} of apples, should bump those up to 6 broseph, that way you can beat the {num_students} students in the apple eating contest")

# Floats = floating point number for example 3.1 

price = 10.99
gpa = 4.00
distance = 5.5

print(f"The price is {price}, currently your GPA is {gpa}, the distance that you can run with coffee is {distance}km's. ")

#Boolean = is either true or false 
is_student = False
for_sale = True
is_online = True

print(f"are you a student?: {is_student}")

if is_student:
    print("keep studying you will be almost done!")
else:
    print("You are not a student, must of finished being awesome kek. ")
    
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
    
if is_online:
    print("The user is currently online.")
else:
    print("The user is currently not online.")