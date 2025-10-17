import math

# Calculating the circle circumference 

# C = 2 x pi x r 

radius = float(input('Enter the radiu of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")

# Area of a circle 

# A = pi x r²

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm²")

# Finding the Hyptoenuse of a right triangle 

# C = sqrt a² + b²

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")