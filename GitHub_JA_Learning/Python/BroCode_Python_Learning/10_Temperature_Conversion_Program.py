unit = input("Is this Temperature in Celsius or Fahrenheit? (C/F): ")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f"The temperature in Fahrenheits is: {temp} °F") 
    # To get the little circle to the left of F press ----> ALT + 0176 (windows option) OR Shift + Option + 8 (Mac Option)
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"The temperature in Celsius is: {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement")