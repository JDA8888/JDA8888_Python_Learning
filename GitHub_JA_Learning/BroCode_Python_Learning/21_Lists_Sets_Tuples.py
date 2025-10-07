# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. duplicates okay
# set = {} unordered and immutable, but add/remove okay, NO DUPLICATES
# Tuple = () ordered and unchangeable. Duplicates OKAY, FASTER

fruit = ["Apple", "Coconut", "Pear", "Banana"]
# Give a list of what can be done, if you want a description use print(help(fruit))
print(dir(fruit))

fruit.append("pineapple")
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])

fruit.remove("Apple")
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])

fruit.insert(0,"pineapple")
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])

fruit.sort()
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])
fruit.reverse()
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])

print(fruit.index("Pear"))
print(fruit[2])
print(fruit[0:2])
print(fruit[::-1])
print(fruit[::2])

for x in fruit:
    print(x)
    

# SETS # 

# You can not use indexing on a set due to sets being unordered. 
fruits = {"Apple", "Coconut", "Pear", "Banana"}

fruits.add("Pineapple")
fruits.remove("Apple")
fruits.pop() # Will be Random
fruits.clear()

print(fruits)


## Tuple ## 

fruit1 = ("Apple", "Coconut", "Pear", "Banana")
print(len(fruit1))
print("pineapple" in fruit1)

print(fruit1.index("Apple"))
print(fruit1.count("Apple"))

for y in fruit1:
    print(y)