# Python compund interest calculator 

# A = final amound, P = initial principal balance, r = interest rate, t = number of time periods elapsed

principle = 0
rate = 0
time = 0

while principle <= 0: 
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Principle can not be less than or equal to zero")
        

while rate <= 0: 
    rate = float(input("Enter a rate amount: "))
    if rate <= 0:
        print("Rate can not be less than or equal to zero")
        
while time <= 0: 
    time = int(input("Enter a time amount: "))
    if time <= 0:
        print("time can not be less than or equal to zero")
        
print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")