# *args = allows you to pass multiple non-key arguments ----- TUPLE --------
# **kwargs = allows you to pass multiple keyword-arguments ------ DICTIONARY -------
# *unpacking operator
# 4. ARBITRARY --- section --- 

def add(*args): # Name can change the important thing here is the * before the name for example we could have *number or *num or *n1 all are fine. 
    total = 0
    for arg in args:
        total += arg # as long as you define them here, e.g. changing args to match e.g. *n1 etc 
    return total
        

print(add(1, 2, 3, 4, 5))
print()
print()

# Example 2 -- 

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Dr.", "John", "Awesome", "Wick", "Movie VIII") 

print()
print()

# Example 3 --- kwargs --- 

def print_address(**kwargs):
    # print(type(kwargs)) # Showing Dictionary 
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_address(street="99 fake street",
              apparment="101010",
            city="Toyko",
            state="Seal",
            zipcode="1234",)

print()
print()

# Example 4 

def shipping_label(*args, **kwargs):  #keyword argument MUST FOLLOW positional arugments, not the other way around -- it wont work if you put poisitonal after keyword arugments -- 
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end= " ")
    if "apparment" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apparment')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zipcode')}")

shipping_label("Dr.", "John", "Wick", "VIII",
               street="123 Fake Street",
               apparment= "# 101",
               city= "Toyko",
               state= "GunLand",
               zipcode="1235")