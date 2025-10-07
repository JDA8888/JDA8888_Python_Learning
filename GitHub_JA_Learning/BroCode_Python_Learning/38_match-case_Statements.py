# Match-case statment (switch): An alternative to using many "elif" statements
# Execute some code if a value matches a 'case' (value == case)
# benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case "Sunday":
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6: 
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: # An underscore in a match case statement is a wild card, it functions as an else statement here. 
            return "Not a Valid Day"
        
# -- Test --    
print(day_of_week(1))
print()

# Example 2  | = or 
def day_of_week(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: # An underscore in a match case statement is a wild card, it functions as an else statement here. 
            return False
        
# -- Test --
print(day_of_week("Saturday"))