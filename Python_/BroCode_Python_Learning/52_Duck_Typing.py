# "Duck Typing" = Anothre way to achieve polymorphism besides Inheritance
# Object must have the minimum necessary attributes / methods
# "If it looks like a duck and quacks like a duck, it must be a duck."

class Animial:
    alive = True
    
class Dog(Animial):
    def speak(self):
        print("WOOF")
        
class Cat(Animial):
    def speak(self):
        print("MEOW")
        
class Car:
    
    alive = False
    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]

for animial in animals:
    animial.speak()
    print(animial.alive)