# List Comprehension = A concise way to create lists in Python
# Compact and easier to red than traditional loops
# [expression for value in iterable if condition]

doubles = []
for x in range(1, 11):  # Rembember that for a range values the 2nd number (11) is exclusive therefore it'll give 1 to 10
    doubles.append(x * 2)
print(doubles)
print()


# Here is how to list comp

doubles = [x * 2 for x in range(1, 11)] # [expression for value in iterable] 
print(doubles)
print()

# Example 1 
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print()
print(triples)
print()
print(squares)
print()

# Example 2 -- Fruits -- 

fruits = ["apples", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits] # [expression for value in iterable] 
fruits_chars = [fruit[0] for fruit in fruits]

print(fruits)
print()
print(fruits_chars)
print()

# Example 3 -- Numbers -- 

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
postive_nums = [num for num in numbers if num >=0] # [expression for value in iterable] 
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(postive_nums)
print()
print(negative_nums)
print()
print(even_nums)
print()
print(odd_nums)
print()

# Example 4 -- Grades -- 

grades = [85, 42, 79, 90, 56, 61, 30,99]

passing_grades_credit = [grade for grade in grades if grade >= 60 and  grade <= 75]
passing_grades_desc = [grade for grade in grades if grade >= 76 and  grade <= 90]
passing_grades_hdesc = [grade for grade in grades if grade >= 91 and  grade <= 100]
failing_grades = [grade for grade in grades if grade <= 50]


print(passing_grades_credit)
print()
print(passing_grades_desc)
print()
print(passing_grades_hdesc)
print()
print(failing_grades)
