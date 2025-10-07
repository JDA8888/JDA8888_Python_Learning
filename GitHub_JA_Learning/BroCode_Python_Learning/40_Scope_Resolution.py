# variable scope = where a variable is bisible and accessible
# Scope resolution = (LEGB rule) =  Local -> Enclosed -> Global -> Built-in

# Example -- 

def func1():
    a = 1 #Local 
    print(a)
    
def func2():
    b = 2
    print(b)
    
x = 3 # Global

# Example --- 

from math import e

def func3():
    print(e)
    
e = 3 

func3()