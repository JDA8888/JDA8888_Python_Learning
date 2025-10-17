# exception = An event that interrupts the flow of a program (ZeroDivisionError, TypeError, ValueError)
# 1. try, 2. except, 3. finally


# try:
    # Try some code
# except Exception:
    # Handle an Exception
# finally:
    # Do some clean up

try:
    number = int(input("Enter a Number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can not divide by zero.... cmon man...")
except ValueError:
    print("Enter only numbers please!")
finally:
    print("Do Some cleanup here")