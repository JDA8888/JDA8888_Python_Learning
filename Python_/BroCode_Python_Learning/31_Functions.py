# Function = A block of reusable code
    # place () after the function name to invoke it
   
   
 # Example 1 --- Happy Birthday Function ----   
def happy_birthday(name, age): 
    print(f"happy birthday to {name}!")
    print(f"You are {age} old")
    print(f"happy birthday to {name}!")
    print()

happy_birthday("Broski", 33)
happy_birthday("Brad", 29)
happy_birthday("Cameron", 29)

# Example 2 ----- Invoice function 

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("BroCode", 100.01, "01/01/1992 \n")

# Example 3 --- Using Return ----- 
# Return = Statment used to end a function and send a result back to the caller

def add(x,y):
    z = x + y 
    return z

def minus(x,y):
    z = x - y 
    return z

def multiple(x,y):
    z = x * y 
    return z

def divide(x,y):
    z = x / y 
    return z

print(add(1,2))
print(minus(1,2))
print(multiple(1,2))
print(divide(1,2))
print()


#Example 4 --- Creating a name ----

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("jack", "ricky")

print(full_name)