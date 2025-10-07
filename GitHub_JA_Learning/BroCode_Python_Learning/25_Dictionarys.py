# Dictionary = a collection of {key:value} pairs
                # Ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "Australia": "Canberra ACT",
            "Russia": "Moscow",
            "India": "New Delhi"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("Australia"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
 
#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
#for key, value in capitals.items():
#    print(f"{key}: ")

    
