# Class methods = Allow operations related to the class itself
# take (cls) as the first parameter, which represents the class itself. 

# Instance methods = best for operations on instances of the class (objects)
# Static methods = best for utility functions that do not need access to class data
# Class methods = best for class-level data or require access to the class itself


class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # This is an Instance Method    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    # This is a class Method
    @classmethod
    def get_count(cls):
        return f"Total #No. of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average Student GPA for course is: {cls.total_gpa / cls.count:.2f}"

student1 = Student("Alex", 3.2)
student2 = Student("Josh", 2.0)
student3 = Student("Jax", 3.99)

    
print(Student.get_count())
print(Student.get_average_gpa())
