# OOP = Object Oriented Programming 

# Object = A "Bundle" of related attributes (variables) and methods (functions)
# Example. Phone, Cup, book
# You need a "Class" to create many objects

# Class = (Blueprint) used to design the structure and layout of an object

from car import Car
        
car1 = Car("Mustang", "2024", "red", False)
car2 = Car("Corvette", "2025", "blue", True)
car3 = Car("Charger", "2026", "Yellow", True)

print(car1.model)
print(car2.year)
print(car3.color)
print(car1.for_sale) #paying close attention to how it is print different cars fields.

car1.drive()
car2.stop()
car3.describe()