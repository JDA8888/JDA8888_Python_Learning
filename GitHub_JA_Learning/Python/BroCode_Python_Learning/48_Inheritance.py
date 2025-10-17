# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps wit code reusability and extensibility 
# class child (Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
        
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("I AM THE MOUSE OF DOOM, I HAVE COME FOR YOUR SOUL!~!")

dog = Dog("Scobby")
cat = Cat("Frankie Jnr")
mouse = Mouse("Micky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
cat.speak()
mouse.speak()