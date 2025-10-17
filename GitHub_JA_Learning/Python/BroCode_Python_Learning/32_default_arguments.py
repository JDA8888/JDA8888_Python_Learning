# default arguments = A deault value for certain parameters, default is used when that arugment is omitted 
# This makes your functions more flexible, reduces $ of arguments 
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# Function for net price -- adding default arugments 

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price *(1 - discount) *(1 + tax)

print(net_price(500))
print()
print(net_price(500, 0.1, 0))


# Next section, even though import time is in this part it is custom to ensure it is at the top of the code file starting, but for this section
# this is the next example 
import time

def count(end, start = 0): # This shows that default argmuments need to be after an input one. 
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)