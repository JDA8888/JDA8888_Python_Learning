# Nested Loop = a loop within another loop (outer, inner) 
    # outer loop:
    # inner loop:
    # print(x, end="") will put everything on the same line. 
    # The blank print statement outside the loop creates a new line. 
    # The basic's of this is a loop inside of a loop. 

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the number of symbol to use: ")

for x in range (rows):
    for y in range(columns):
        print(symbol, end="")
    print()
    

    
