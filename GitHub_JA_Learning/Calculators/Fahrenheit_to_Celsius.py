# Simple Fahrenheit to Celisus caculation 
fahrenheit = float(input("Please type in a temperature (F): "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")