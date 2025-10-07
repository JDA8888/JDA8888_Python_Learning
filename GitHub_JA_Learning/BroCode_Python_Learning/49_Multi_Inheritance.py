# Multiple inheritance = inherit from more than one parent class C(A,B)
# Multilevel inheritance = inherit from a parent which inherits from another parent 
# C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is Eating...")
    def sleep (self):
        print(f"{self.name} is sleeping...")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is FLEEING !!! ")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting....")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Neomo")



## TESTING ## 
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

rabbit.eat()