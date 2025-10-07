# A 2-d List is just a list made up of lists, kind of like a excell spreedsheet

fruits =     ["apple", "pear", "coconut", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "turkey", "beef"]

groceries = [fruits, vegetables, meats]
# Like a matrix, finding the subject required for example below gives you coconuts
print(groceries[0][2])


for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()