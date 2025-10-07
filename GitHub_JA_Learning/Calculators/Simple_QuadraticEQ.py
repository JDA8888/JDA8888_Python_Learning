
from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

quad_eq1 =(-b + sqrt(b**2 - 4*a*c))/(2*a)
quad_eq2 =(-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f"The Roots are {quad_eq1} and {quad_eq2}")

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5