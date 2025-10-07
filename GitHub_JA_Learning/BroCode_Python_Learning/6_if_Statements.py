# if = Do some code only IF some condition is True
    # Else do something else
    
age = int(input("enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You havent even been born yet.")
elif age >= 100:
    print("You are too old to sign up, what would be the point? ")
else: 
    age <= 18
    print("You are to young for a credit card, You must be 18+ to sign-up. ")
    
    
response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Have some food then")
else:
    response == "N"
    print("No food for you then.")
    
    
name = input("Enter your name: ")

if name == "":
    print("YOU DIDNT TYPE IN YOUR NAME!")
else:
    print(f"Hello {name}")
    

# BOOLEAN WITH IF STATEMENTS

for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale. ")