# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reuseable separate files

# for usefule functions you can print the help function for modules e.g. below: 

# print(help("modules"))
# you can then place the name of the module in the help function e.g.
#print(help("math")) <--- which gives a description

import example39
import math

import math as m # <-- Helps you to reduce nameing and ensure this file using the 'm' as math
from math import pi # <-- imports pi from math

print(math.pi)
print()

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print()
print(math.e ** b)
print()
print(math.e ** c)
print()
print(math.e ** d)
print()

# for this example e will be the version that is used that we created, better to put math infront just as a precaution. 

print(e ** e)
print()

result1 = example39.pi
result2 = example39.sqaure(3)
result3 = example39.cube(3)
result3 = example39.circumference(3)
result4 = example39.area(3)

print(result1)
print()
print(result2)
print()
print(result3)
print()
print(result4)
