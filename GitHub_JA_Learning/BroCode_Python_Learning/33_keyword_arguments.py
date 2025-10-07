# keyword arugments = an arugment preceded by an identifier which helps with readability
# order of aruments doesnt matter
# Section 2. - KEYWORD
print()
def hello(greeting, title, firstname, lastname):
    print(f"{greeting} {title} {firstname} {lastname}")
    
hello("Hello", title="Mr", lastname="Wick", firstname="John") # Positional arugments need to be first, as seen in this example. 
# -- Additionally using the argument in this line allows it to be a keyword which means it can be in any order. 
print()

# Example 2. 

for x in range(1, 11):
    print(x, end=" ")
    
# Example 3. -- Seperate --- 

print("1", "2", "3", "4", "5", sep="--")
print()
#Example 4 -- Exercise -- 

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country=1, area=123, first=456, last=7890 )

print(phone_number)