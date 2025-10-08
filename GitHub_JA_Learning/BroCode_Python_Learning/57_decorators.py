# Decorator = A function that extends the behavior of another function, w/o modifying the base function
# Pass the base function as an argument to the decorator

# @add_sprinkles
# get_ice_cream("vanilla")

def add_sprinkles(function):
    def wrapper(*args, **kwargs):
        print("* You have Added Sprinkles 🌟")
        function(*args, **kwargs)
    return wrapper

def add_choc(func):
    def wrapper(*args, **kwargs):
        print("You have added Chocolate 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_choc
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice-cream🍧 ")
    
get_ice_cream("Vanilla")