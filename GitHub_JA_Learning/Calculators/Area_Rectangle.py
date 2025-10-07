# Exercise 1, Calc the area of a rectangle

# To create cm^2 press Numlock + ALT + 0178

length = float(input("Enter the length: "))
Width = float(input("Enter the Width: "))

Area = length * Width

print(f"The Area is: {Area} cm²")

# Exercise 2, Creating a shopping cart program 

item = input("What item would you like to buy today?: ")
price = float(input("What is the price?: "))
quantity = int(input("how many would you like to buy today?: "))
total = price * quantity

print(total)

print(f"You have brought {quantity} x {item}/s ")
print(f"Your total is: ${total}")