# Iterables = An object / collection that can return its elements one at a time, allow it to be iterated over in a loop. 

numbers = [1, 2, 3, 4, 5] # This is a list, Tuples e.g. (1,2,3,4,5) can also work. 

for number in numbers:
    print(number)

print()    
for number in reversed(numbers): # Reverses the numbers 
    print(number, end= " - ")
print()
    
# Example Set

fruits = {"apple", "orange", "banana", "coconut"}
# Note: Sets are not reverseable. doesnt work. 
for fruit in fruits:
    print(fruit)
print()    
    
name = "John Wick"
for character in name:
    print(character, end= " ")

print()
print()
    
# Dictonaries 

my_dictonary = {"A":1, "B": 2, "C": 3}

for key, value in my_dictonary.items():
    print(f"{key} = {value}")