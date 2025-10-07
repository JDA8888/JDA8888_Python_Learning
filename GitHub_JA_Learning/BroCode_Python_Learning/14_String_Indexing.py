# Indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"

#print(credit_number[0])

#Start of string, 0 is not required
#print(credit_number [0:4])

#printing middle of string
#print(credit_number [5:9])

# Assume up to the end of the string
#print(credit_number[5:])

# Prints the number starting from the back to front
#print(credit_number[-1])
# Adding steps which counts every 2nd character. 

#print(credit_number[::2])


## Creating a program to get the last four digits of a credit card number

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")