# Class variables = shared among all instances of a class
# defined outside the constructor and allows you to share data among all objects created from that class


class Student:
    
    class_year= 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Frank", 33)
student2 = Student("Alex", 28)
student3 = Student("Jack", 45)
student4 = Student("John", 27)


print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student1.class_year)
print(student2.class_year)
print(Student.class_year) # Helps being clear, accessing the class not any instance from the class

print(Student.num_students)


# Exercise 

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)