# for loops = execute a block of code a fixed number of time.
    # You can iterate over a rage, string, sequence, etc. 

for x in range(1, 11):
    print(x)
print("Happy NEW YEAR! ! !")

for x in reversed(range(1, 11)):
    print(x)
print("Happy NEW YEAR! ! !")

for x in (range(1, 11, 3)):
    print(x)

# Example 

credit_card_number = "1234-5678-9012-3456"
for y in credit_card_number:
    print(y)
    
    
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)